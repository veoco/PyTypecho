from xmlrpc.client import ServerProxy
from typing import List, Dict, Optional

from .utils import try_rpc


class TypechoPostMixin:
    def get_posts(self, num: int = 10) -> Optional[List[Dict]]:
        return try_rpc(self.s.metaWeblog.getRecentPosts, self.blog_id, self.username, self.password, num)

    def get_post(self, post_id: int) -> Optional[Dict]:
        return try_rpc(self.s.metaWeblog.getPost, post_id, self.username, self.password)

    def new_post(self, p_content, publish: bool) -> Optional[str]:
        """
        Content's status will cover publish, and if you only save post, the post id will only be '0'
        If content's categories are not created, it will only create the first category
        """
        post = p_content.as_post()
        return try_rpc(self.s.metaWeblog.newPost, self.blog_id, self.username, self.password, post, publish)

    def edit_post(self, p_content, publish: bool) -> Optional[str]:
        return self.new_post(p_content, publish)

    def del_post(self, post_id: int) -> None:
        return try_rpc(self.s.blogger.deletePost, self.blog_id, post_id, self.username, self.password, True)


class TypechoPageMixin:
    def get_pages(self) -> Optional[List[Dict]]:
        return try_rpc(self.s.wp.getPages, self.blog_id, self.username, self.password)

    def get_page(self, page_id: int) -> Optional[Dict]:
        return try_rpc(self.s.wp.getPage, self.blog_id, page_id, self.username, self.password)

    def new_page(self, p_content, publish: bool) -> Optional[str]:
        """
        Content's status will cover publish, and if you only save post, the post id will only be '0'
        """
        page = p_content.as_page()
        return try_rpc(self.s.metaWeblog.newPost, self.blog_id, self.username, self.password, page, publish)

    def edit_page(self, p_content, publish: bool) -> Optional[str]:
        return self.new_page(p_content, publish)

    def del_page(self, page_id: int) -> Optional[bool]:
        return try_rpc(self.s.wp.deletePage, self.blog_id, self.username, self.password, page_id)


class TypechoCategoryMixin:
    def get_categories(self) -> Optional[Dict]:
        return try_rpc(self.s.metaWeblog.getCategories, self.blog_id, self.username, self.password)

    def new_category(self, name: str, slug: str = None, parent: int = 0, description: str = None) -> Optional[str]:
        category = {'name': name}
        if slug:
            category.update({'slug': slug})
        if parent:
            category.update({'parent': parent})
        if description:
            category.update({'description': description})
        return try_rpc(self.s.wp.newCategory, self.blog_id, self.username, self.password, category)

    def del_category(self, category_id: int) -> Optional[bool]:
        return try_rpc(self.s.wp.deleteCategory, self.blog_id, self.username, self.password, category_id)


class TypechoTagMixin:
    def get_tags(self) -> Optional[List[Dict]]:
        return try_rpc(self.s.wp.getTags, self.blog_id, self.username, self.password)


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
        return try_rpc(self.s.wp.getMediaLibrary, self.blog_id, self.username, self.password, struct)

    def get_attachment(self, attachment_id) -> Optional[Dict]:
        return try_rpc(self.s.wp.getMediaItem, self.blog_id, self.username, self.password, attachment_id)

    def new_attachment(self, file_name, file_byte):
        data = {
            'name': file_name,
            'bytes': file_byte
        }
        return try_rpc(self.s.wp.uploadFile, self.blog_id, self.username, self.password, data)


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
        return try_rpc(self.s.wp.getComments, self.blog_id, self.username, self.password, struct)

    def get_comment(self, comment_id: int) -> Optional[Dict]:
        return try_rpc(self.s.wp.getComment, self.blog_id, self.username, self.password, comment_id)

    def new_comment(self, post_id: int, author: str, comment_content: str, author_email: str = None,
                    author_url: str = None,
                    comment_parent: str = None) -> None:
        struct = {
            'comment_author': 1,
            'author': author,
            'content': comment_content
        }
        if author_email:
            struct.update({'comment_author_email': 1, 'author_email': author_email, })
        if author_url:
            struct.update({'comment_author_url': 1, 'author_url': author_url})
        if comment_parent:
            struct.update({'comment_parent': comment_parent})
        return try_rpc(self.s.wp.newComment, self.blog_id, self.username, self.password, post_id, struct)

    def edit_comment(self, comment_id: int, author: str, comment_content: str, author_email: str = None,
                     status: str = None, author_url: str = None) -> Optional[bool]:
        struct = {
            'author': author,
            'content': comment_content
        }
        if author_email:
            struct.update({'author_email': author_email, })
        if status:
            struct.update({'status': status})
        if author_url:
            struct.update({'author_url': author_url})
        return try_rpc(self.s.wp.editComment, self.blog_id, self.username, self.password, comment_id, struct)

    def del_comment(self, comment_id: int) -> Optional[bool]:
        return try_rpc(self.s.wp.deleteComment, self.blog_id, self.username, self.password, comment_id,)


class Typecho(TypechoPostMixin, TypechoPageMixin, TypechoCategoryMixin, TypechoTagMixin, TypechoAttachmentMixin,
              TypechoCommentMixin):
    def __init__(self, rpc_url: str, username: str, password: str):
        self.rpc_url = rpc_url
        self.username = username
        self.password = password

        self.s = ServerProxy(rpc_url)
        # blog id could be any number.
        self.blog_id = 1