import os
import pytest

from pytypecho import Typecho


@pytest.fixture(scope="module")
def te():
    return Typecho(
        rpc_url=os.environ.get("XMLRPC_URL"),
        username=os.environ.get("XMLRPC_USER_NAME"),
        password=os.environ.get("XMLRPC_USER_PASSWORD"),
        debug=True,
    )
