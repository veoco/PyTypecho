import sys
import urllib
import asyncio

from xmlrpc.client import dumps, loads


__version__ = "%d.%d" % sys.version_info[:2]


class _AsyncMethod:
    def __init__(self, send, name):
        self.__send = send
        self.__name = name

    def __getattr__(self, name):
        return _AsyncMethod(self.__send, "%s.%s" % (self.__name, name))

    async def __call__(self, *args):
        return await self.__send(self.__name, args)


class AsyncResponse:
    def __init__(self, reader: asyncio.StreamReader) -> None:
        self.reader = reader
        self.encoding = "utf-8"

        self.version = None
        self.status_code = None
        self.reason_phrase = None
        self.header = {}
        self.content_length = 0
        self.content = None

    @property
    def text(self):
        return self.content.decode(self.encoding)

    async def parse_start_line(self):
        start_line = await self.reader.readline()
        start_line = start_line.decode(self.encoding).rstrip("\r\n")
        self.version, self.status_code, self.reason_phrase = start_line.split()

    async def parse_header(self):
        header_line = await self.reader.readline()
        while header_line != b"\r\n":
            if header_line:
                header_line = header_line.decode(self.encoding).rstrip("\r\n").rstrip()
                name, value = header_line.split(": ")
                self.header.update({name: value})
            header_line = await self.reader.readline()

    async def parse_body(self):
        if self.header.get("Transfer-Encoding", None):
            while True:
                length_line = await self.reader.readline()
                length_line = length_line.decode(self.encoding).rstrip("\r\n")
                if length_line == "0":
                    break
                self.content_length += int(length_line, 16)

                content_line = await self.reader.readline()
                content_line = content_line.rstrip(b"\r\n")
                if self.content is None:
                    self.content = content_line
                else:
                    self.content += content_line
        elif self.header.get("Content-Length", None):
            self.content_length = int(self.header["Content-Length"])
            self.content = await self.reader.readexactly(self.content_length)

    async def parse(self):
        await self.parse_start_line()
        await self.parse_header()
        await self.parse_body()


class AsyncServerProxy:
    user_agent = "Python-xmlrpc/%s" % __version__

    def __init__(self, uri: str, semaphore: int):
        p = urllib.parse.urlsplit(uri)
        if p.scheme not in ("http", "https"):
            raise OSError("unsupported XML-RPC protocol")
        else:
            if p.scheme == "https":
                self.ssl = True
                self.port = p.port or 443
            else:
                self.ssl = False
                self.port = p.port or 80
        self.host = p.netloc
        self.hostname = p.hostname
        self.handler = urllib.parse.urlunsplit(["", "", *p[2:]])
        self.encoding = "utf-8"

        self.semaphore = asyncio.Semaphore(semaphore)

    async def make_connection(self):
        await self.semaphore.acquire()
        reader, writer = await asyncio.open_connection(
            self.hostname, self.port, ssl=self.ssl
        )
        connection = reader, writer
        return connection

    async def _request(self, request_body):
        reader, writer = await self.make_connection()
        request_head = (
            f"POST {self.handler} HTTP/1.1\r\n"
            f"Host: {self.host}\r\n"
            f"User-Agent: {self.user_agent}\r\n"
            f"Content-Type: text/xml\r\n"
            f"Content-Length: {len(request_body)}\r\n"
            f"\r\n"
        ).encode("utf-8")
        request = request_head + request_body
        writer.write(request)
        await writer.drain()

        response = AsyncResponse(reader)
        await response.parse()

        writer.close()
        await writer.wait_closed()
        self.semaphore.release()

        u, methodname = loads(response.text)
        return u

    async def request(self, method_name, params):
        request = dumps(
            params, method_name, encoding=self.encoding, allow_none=False
        ).encode(self.encoding, "xmlcharrefreplace")

        response = await self._request(request)

        if len(response) == 1:
            response = response[0]

        return response

    def __getattr__(self, name):
        return _AsyncMethod(self.request, name)
