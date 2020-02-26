from xmlrpc.client import ServerProxy, Fault
from typing import List, Dict, Optional
from dataclasses import asdict

from .log import logger
from .models import Post, Page, Category, Attachment, Comment


class TypechoPostMixin:
    def get_posts(self, num: int = 10) -> Optional[List[Dict]]:
        return self.try_rpc(self.s.metaWeblog.getRecentPosts, num)

    def get_post(self, post_id: int) -> Optional[Dict]:
        return self.try_rpc(self.s.metaWeblog.getPost, post_id)

    def new_post(self, post: Post, publish: bool) -> Optional[str]:
        """
        Post's status will cover publish, and if you only save post, the post id will only be '0'
        If Post's categories are not created, it will only create the first category
        """
        return self.try_rpc(self.s.metaWeblog.newPost, post, publish)

    def edit_post(self, post: Post, post_id: int, publish: bool) -> Optional[str]:
        d = asdict(post)
        d.update({'postId': post_id})
        return self.try_rpc(self.s.metaWeblog.newPost, d, publish)

    def del_post(self, post_id: int) -> None:
        return self.try_rpc(self.s.blogger.deletePost, post_id)


class TypechoPageMixin:
    def get_pages(self) -> Optional[List[Dict]]:
        return self.try_rpc(self.s.wp.getPages)

    def get_page(self, page_id: int) -> Optional[Dict]:
        """
        WARNING: Different from other API!
        """
        return self._try_rpc(self.s.wp.getPage, self.blog_id, page_id, self.username, self.password)

    def new_page(self, page: Page, publish: bool) -> Optional[str]:
        """
        Page's status will cover publish, and if you only save post, the post id will only be '0'
        """
        return self.try_rpc(self.s.metaWeblog.newPost, page, publish)

    def edit_page(self, page: Page, page_id: int, publish: bool) -> Optional[str]:
        d = asdict(page)
        d.update({'postId': page_id})
        return self.try_rpc(self.s.metaWeblog.newPost, d, publish)

    def del_page(self, page_id: int) -> Optional[bool]:
        return self.try_rpc(self.s.wp.deletePage, page_id)


class TypechoCategoryMixin:
    def get_categories(self) -> Optional[Dict]:
        return self.try_rpc(self.s.metaWeblog.getCategories)

    def new_category(self, category: Category, parent_id: int = 0) -> Optional[str]:
        return self.try_rpc(self.s.wp.newCategory, category)

    def del_category(self, category_id: int) -> Optional[bool]:
        return self.try_rpc(self.s.wp.deleteCategory, category_id)


class TypechoTagMixin:
    def get_tags(self) -> Optional[List[Dict]]:
        return self.try_rpc(self.s.wp.getTags)


class TypechoAttachmentMixin:
    def get_attachments(self, post_id: int = None, mime_type: str = None, page_size: int = None,
                        page_num: int = None) -> Optional[List[Dict]]:
        struct = {}
        if post_id:
            struct.update({'parent_id': post_id})
        if mime_type:
            struct.update({'mime_type': mime_type})
        if page_size:
            struct.update({'number': page_size})
        if page_num:
            struct.update({'offset': page_num})
        return self.try_rpc(self.s.wp.getMediaLibrary, struct)

    def get_attachment(self, attachment_id) -> Optional[Dict]:
        return self.try_rpc(self.s.wp.getMediaItem, attachment_id)

    def new_attachment(self, data: Attachment):
        return self.try_rpc(self.s.wp.uploadFile, data)


class TypechoCommentMixin:
    def get_comments(self, status: str = None, post_id: int = None, page_size: int = None,
                     page_num: int = None) -> Optional[List[Dict]]:
        struct = {}
        if status:
            struct.update({'status': status})
        if post_id:
            struct.update({'parent_id': post_id})
        if page_size:
            struct.update({'number': page_size})
        if page_num:
            struct.update({'offset': page_num})
        return self.try_rpc(self.s.wp.getComments, struct)

    def get_comment(self, comment_id: int) -> Optional[Dict]:
        return self.try_rpc(self.s.wp.getComment, comment_id)

    def new_comment(self, comment: Comment, post_id: int, comment_parent: str = None) -> None:
        d = asdict(comment)
        if comment_parent:
            d.update({'comment_parent': comment_parent})
        path = post_id
        return self.try_rpc(self.s.wp.newComment, path, d)

    def edit_comment(self, comment: Comment, comment_id: int) -> Optional[bool]:
        return self.try_rpc(self.s.wp.editComment, comment_id, comment)

    def del_comment(self, comment_id: int) -> Optional[bool]:
        return self.try_rpc(self.s.wp.deleteComment, comment_id, )


class Typecho(TypechoPostMixin, TypechoPageMixin, TypechoCategoryMixin, TypechoTagMixin, TypechoAttachmentMixin,
              TypechoCommentMixin):
    def __init__(self, rpc_url: str, username: str, password: str):
        self.rpc_url = rpc_url
        self.username = username
        self.password = password

        self.s = ServerProxy(rpc_url)
        # blog id could be any number.
        self.blog_id = 1

    def try_rpc(self, rpc_method, *args, **kw):
        return self._try_rpc(rpc_method, self.blog_id, self.username, self.password, *args, **kw)

    def _try_rpc(self, rpc_method, *args, **kw):
        res = None
        try:
            res = rpc_method(*args, **kw)
            logger.info(res)
            if res == '':
                res = None
        except Fault as e:
            logger.error("Error {}: {}".format(e.faultCode, e.faultString))
        except Exception as e:
            logger.error("Error {}".format(e))
        finally:
            return res
