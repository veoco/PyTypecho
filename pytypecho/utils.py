from xmlrpc.client import Fault
from typing import List, Dict


def try_rpc(rpc_method, *args, **kw):
    res = None
    try:
        res = rpc_method(*args, **kw)
        if res == '':
            res = None
    except Fault as e:
        print("Error {}: {}".format(e.faultCode, e.faultString))
    finally:
        return res


class Content:
    def __init__(self, title: str, description: str, slug: str = '', text_more: str = '', password: str = '',
                 order: int = 0, tags: str = '', categories: List[str] = None, post_id: int = 0,
                 created: str = '', template: str = '', allow_comment: int = 1, allow_ping: int = 1,
                 allow_feed: int = 1, status: str = ''):
        """
        Post needs at least: title, description , category.
        Page needs at least: title, description.

        text_more will be connected with description as description+'\n<!--more-->\n'+text_more by Typecho.
        tags should be split by ',' like 'tag1, tag2'
        created should be timestamp.
        allow_feed has no effect because Typecho not use
        status could be 'publish' or 'save' or 'private'.
        """

        self.title = title
        self.description = description

        self.slug = slug
        self.text_more = text_more
        self.password = password
        self.order = order
        self.tags = tags
        self.categories = categories or []
        self.post_id = post_id
        self.created = created
        self.template = template
        self.allow_comment = allow_comment
        self.allow_ping = allow_ping
        self.allow_feed = allow_feed
        self.status = status

    def as_post(self) -> Dict:
        res = {
            'post_type': 'post',
            'title': self.title,
            'description': self.description,
            'slug': self.slug,
            'mt_text_more': self.text_more,
            'wp_password': self.password,
            'mt_keywords': self.tags,
            'categories': self.categories,
            'created': self.created,
            'mt_allow_comments': self.allow_comment,
            'mt_allow_pings': self.allow_ping,
            'post_status': self.status
        }
        if self.post_id != 0:
            res.update({'postId': self.post_id})
        return res

    def as_page(self) -> Dict:
        res = {
            'post_type': 'page',
            'title': self.title,
            'description': self.description,
            'slug': self.slug,
            'mt_text_more': self.text_more,
            'wp_password': self.password,
            'wp_page_order': self.order,
            'mt_keywords': self.tags,
            'created': self.created,
            'wp_page_template': self.template,
            'mt_allow_comments': self.allow_comment,
            'mt_allow_pings': self.allow_ping,
            'post_status': self.status
        }
        if self.post_id != 0:
            res.update({'postId': self.post_id})
        if self.order != 0:
            res.update({'wp_page_order': self.order})
        return res
