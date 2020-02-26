import pytest

from pytypecho import Typecho


@pytest.fixture(scope="module")
def te():
    return Typecho('http://192.168.50.70:8080/index.php/action/xmlrpc', username='admin', password='admin')
    # return Typecho('http://127.0.0.1:4567/index.php/action/xmlrpc', username='admin', password='admin')
