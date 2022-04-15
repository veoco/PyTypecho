import os
import unittest

from pytypecho import Typecho, Post, Page, Category, Comment, Attachment


class TypechoTestCase(unittest.TestCase):
    def setUp(self):
        self.te = Typecho(
            rpc_url=os.environ.get("XMLRPC_URL"),
            username=os.environ.get("XMLRPC_USER_NAME"),
            password=os.environ.get("XMLRPC_USER_PASSWORD"),
            debug=os.environ.get("TEST_DEBUG", False),
        )


class TypechoPostTestCase(TypechoTestCase):
    def test_get_post(self):
        r = self.te.get_post(1)
        self.assertIsNotNone(r)

    def test_get_posts(self):
        r = self.te.get_posts()
        self.assertIsNotNone(r)

    def test_new_post(self):
        post = Post(title="Post Title", description="Post Description")
        r = self.te.new_post(post, publish=True)
        self.assertIsNotNone(r)
        self.assertIs(type(r), int)

    def test_edit_post(self):
        post = Post(title="Post Title", description="Post Description")
        num = self.te.new_post(post, publish=True)
        post_edited = Post(
            title="Edited Post Title", description="Edited Post Description"
        )
        r = self.te.edit_post(post_edited, post_id=int(num), publish=True)
        self.assertIsNotNone(r)
        self.assertEqual(r, num)

    def test_del_post(self):
        post = Post(title="Del Post Title", description="Del Post Description")
        num = self.te.new_post(post, publish=True)
        r = self.te.del_post(int(num))
        self.assertIsNotNone(r)


class TypechoPageTestCase(TypechoTestCase):
    def test_get_page(self):
        r = self.te.get_page(2)
        self.assertIsNotNone(r)

    def test_get_pages(self):
        r = self.te.get_pages()
        self.assertIsNotNone(r)

    def test_new_page(self):
        page = Page(title="Page Title", description="Page Description")
        r = self.te.new_page(page, publish=True)
        self.assertIsNotNone(r)
        self.assertIs(type(r), int)

    def test_edit_page(self):
        page = Page(title="Page Title", description="Page Description")
        num = self.te.new_page(page, publish=True)
        page_edited = Page(
            title="Edited Page Title", description="Edited Page Description"
        )
        r = self.te.edit_page(page_edited, page_id=int(num), publish=True)
        self.assertIsNotNone(r)
        self.assertEqual(r, num)

    def test_del_post(self):
        page = Page(title="Del Page Title", description="Del Page Description")
        num = self.te.new_page(page, publish=True)
        r = self.te.del_page(int(num))
        self.assertIsNotNone(r)


class TypechoCategoryTestCase(TypechoTestCase):
    def test_get_category(self):
        r = self.te.get_categories()
        self.assertIsNotNone(r)
        self.assertEqual(r[0]["categoryName"], "默认分类")

    def test_del_category(self):
        r = self.te.del_category(2)
        self.assertIsNotNone(r)


class TypechoTagTestCase(TypechoTestCase):
    def test_get_tags(self):
        r = self.te.get_tags()
        self.assertCountEqual(r, [])


class TypechoCommentTestCase(TypechoTestCase):
    def test_get_comment(self):
        r = self.te.get_comment(1)
        self.assertIsNotNone(r)
        self.assertEqual(r["author"], "Typecho")

    def test_get_comments(self):
        r = self.te.get_comments()
        self.assertIsNotNone(r)
        self.assertEqual(r[0]["content"], "欢迎加入 Typecho 大家族")


class TypechoAttachementTestCase(TypechoTestCase):
    def test_get_attachments(self):
        r = self.te.get_attachments()
        self.assertCountEqual(r, [])
