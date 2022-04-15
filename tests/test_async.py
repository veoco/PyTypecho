import os
import unittest

from pytypecho import AsyncTypecho, Post, Page, Category, Comment, Attachment


class AsyncTypechoTestCase(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.te = AsyncTypecho(
            rpc_url=os.environ.get("XMLRPC_URL"),
            username=os.environ.get("XMLRPC_USER_NAME"),
            password=os.environ.get("XMLRPC_USER_PASSWORD"),
        )


class AsyncTypechoPostTestCase(AsyncTypechoTestCase):
    async def test_get_post(self):
        r = await self.te.get_post(1)
        self.assertIsNotNone(r)

    async def test_get_posts(self):
        r = await self.te.get_posts()
        self.assertIsNotNone(r)

    async def test_new_post(self):
        post = Post(title="Post Title", description="Post Description")
        r = await self.te.new_post(post, publish=True)
        self.assertIsNotNone(r)
        self.assertIs(type(r), int)

    async def test_edit_post(self):
        post = Post(title="Post Title", description="Post Description")
        num = await self.te.new_post(post, publish=True)
        post_edited = Post(
            title="Edited Post Title", description="Edited Post Description"
        )
        r = await self.te.edit_post(post_edited, post_id=int(num), publish=True)
        self.assertIsNotNone(r)
        self.assertEqual(r, num)

    async def test_del_post(self):
        post = Post(title="Del Post Title", description="Del Post Description")
        num = await self.te.new_post(post, publish=True)
        r = await self.te.del_post(int(num))
        self.assertIsNotNone(r)


class AsyncTypechoPageTestCase(AsyncTypechoTestCase):
    async def test_get_page(self):
        r = await self.te.get_page(2)
        self.assertIsNotNone(r)

    async def test_get_pages(self):
        r = await self.te.get_pages()
        self.assertIsNotNone(r)

    async def test_new_page(self):
        page = Page(title="Page Title", description="Page Description")
        r = await self.te.new_page(page, publish=True)
        self.assertIsNotNone(r)
        self.assertIs(type(r), int)

    async def test_edit_page(self):
        page = Page(title="Page Title", description="Page Description")
        num = await self.te.new_page(page, publish=True)
        page_edited = Page(
            title="Edited Page Title", description="Edited Page Description"
        )
        r = await self.te.edit_page(page_edited, page_id=int(num), publish=True)
        self.assertIsNotNone(r)
        self.assertEqual(r, num)

    async def test_del_post(self):
        page = Page(title="Del Page Title", description="Del Page Description")
        num = await self.te.new_page(page, publish=True)
        r = await self.te.del_page(int(num))
        self.assertIsNotNone(r)


class AsyncTypechoCategoryTestCase(AsyncTypechoTestCase):
    async def test_get_category(self):
        r = await self.te.get_categories()
        self.assertIsNotNone(r)
        self.assertEqual(r[0]["categoryName"], "默认分类")

    async def test_del_category(self):
        r = await self.te.del_category(2)
        self.assertIsNotNone(r)


class AsyncTypechoTagTestCase(AsyncTypechoTestCase):
    async def test_get_tags(self):
        r = await self.te.get_tags()
        self.assertCountEqual(r, [])


class AsyncTypechoCommentTestCase(AsyncTypechoTestCase):
    async def test_get_comment(self):
        r = await self.te.get_comment(1)
        self.assertIsNotNone(r)
        self.assertEqual(r["author"], "Typecho")

    async def test_get_comments(self):
        r = await self.te.get_comments()
        self.assertIsNotNone(r)
        self.assertEqual(r[0]["content"], "欢迎加入 Typecho 大家族")


class AsyncTypechoAttachementTestCase(AsyncTypechoTestCase):
    async def test_get_attachments(self):
        r = await self.te.get_attachments()
        self.assertCountEqual(r, [])
