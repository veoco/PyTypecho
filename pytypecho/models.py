from dataclasses import dataclass, field
from typing import List, BinaryIO


@dataclass
class Meta:
    name: str
    parent: int = 0
    slug: str = ''
    description: str = ''


@dataclass
class Category(Meta):
    pass


@dataclass
class Tag(Meta):
    pass


@dataclass
class Content:
    """
    Post needs at least: title, description , category.
    Page needs at least: title, description.

    text_more will be connected with description as description+'\n<!--more-->\n'+text_more by Typecho.
    tags should be split by ',' like 'tag1, tag2'
    created should be timestamp.
    allow_feed has no effect because Typecho not use
    status could be 'publish' or 'save' or 'private'.
    """
    title: str
    description: str

    slug: str = ''
    mt_text_more: str = ''
    wp_password: str = ''
    mt_keywords: str = ''
    created: str = ''
    mt_allow_comments: int = 1
    mt_allow_pings: int = 1
    post_status: str = ''


@dataclass
class Post(Content):
    post_type: str = 'post'
    categories: List[str] = field(default_factory=list)


@dataclass
class Page(Content):
    post_type: str = 'page'
    wp_page_order: int = 0
    wp_page_template: str = ''


@dataclass
class Attachment:
    name: str
    bytes: BinaryIO


@dataclass
class Comment:
    content: str

    author: str = ''
    author_email: str = ''
    author_url: str = ''

    comment_author: int = 0
    comment_author_email: int = 0
    comment_author_url: int = 0

    def __post_init__(self):
        if self.author:
            self.comment_author = 1
        if self.author_email:
            self.comment_author_email = 1
        if self.author_url:
            self.comment_author_url = 1
