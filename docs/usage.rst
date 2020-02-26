Usage
=====================================
First, you should create a Typecho Object:

::

    from pytypecho import Typecho
    te = Typecho('http://127.0.0.1:4567/index.php/action/xmlrpc', username='admin', password='admin')

Post
------------------

Get Post
`````````
A post id(cid) is required.

>>> te.get_post(1)
{'categories': ['默认分类'],
 'custom_fields': [],
 'dateCreated': <DateTime '20200131T14:10:16' at 0x2358a754190>,
 'date_created_gmt': <DateTime '20200131T06:10:16' at 0x2358a754430>,
 'description': '<p>如果您看到这篇文章,表示您的 blog 已经安装成功.</p>',
 'link': 'http://192.168.50.70/index.php/archives/1/',
 'mt_allow_comments': 1,
 'mt_allow_pings': 1,
 'mt_excerpt': '如果您看到这篇文章,表示您的 blog 已经安装成功.',
 'mt_keywords': '',
 'mt_text_more': '',
 'permaLink': 'http://192.168.50.70/index.php/archives/1/',
 'post_status': 'publish',
 'postid': '1',
 'sticky': 0,
 'title': '欢迎使用 Typecho',
 'userid': '1',
 'wp_author': 'admin',
 'wp_author_display_name': 'admin',
 'wp_author_id': '1',
 'wp_password': '',
 'wp_slug': 'start'}

Get Posts
`````````
The post count is optional

>>> te.get_posts()
[{'categories': ['默认分类'],
  'custom_fields': [],
  'dateCreated': <DateTime '20200131T14:10:16' at 0x1b41c9542b0>,
  'date_created_gmt': <DateTime '20200131T06:10:16' at 0x1b41c954430>,
  'date_modified': <DateTime '20200131T14:10:16' at 0x1b41c9544c0>,
  'date_modified_gmt': <DateTime '20200131T06:10:16' at 0x1b41c954520>,
  'description': '<p>如果您看到这篇文章,表示您的 blog 已经安装成功.</p>',
  'link': 'http://192.168.50.70/index.php/archives/1/',
  'mt_allow_comments': 1,
  'mt_allow_pings': 1,
  'mt_excerpt': '如果您看到这篇文章,表示您的 blog 已经安装成功.',
  'mt_keywords': '',
  'mt_text_more': '',
  'permaLink': 'http://192.168.50.70/index.php/archives/1/',
  'post_status': 'publish',
  'postid': '1',
  'sticky': 0,
  'title': '欢迎使用 Typecho',
  'userid': '1',
  'wp_author': 'admin',
  'wp_author_display_name': 'admin',
  'wp_author_id': '1',
  'wp_more_text': '',
  'wp_password': '',
  'wp_post_format': 'standard',
  'wp_post_thumbnail': '',
  'wp_slug': 'start'}
  ...
]

New Post
`````````
You should create a Post instance at first.

>>> post = Post(title='Post Title', description='Post Description')
>>> te.new_post(post, publish=True)
'3'

Edit Post
`````````
You should create a Post instance at first. And specific a post id(cid).

>>> post = Post(title='Edited Post Title', description='Edited Post Description')
>>> te.edit_post(post, post_id='3' publish=True)
'3'

Delete Post
`````````````
A post id(cid) is required.

>>> te.del_post(3)
None

Page
------------------

Get Page
`````````
A page id(cid) is required.

>>> te.get_page(2)
{'categories': [],
 'custom_fields': [],
 'dateCreated': <DateTime '20200131T14:10:16' at 0x1cc50b44190>,
 'date_created_gmt': <DateTime '20200131T06:10:16' at 0x1cc50b44460>,
 'description': '<p>本页面由 Typecho 创建, 这只是个测试页面.</p>',
 'excerpt': '本页面由 Typecho 创建, 这只是个测试页面.',
 'link': 'http://192.168.50.70/index.php/start-page.html',
 'mt_allow_comments': 1,
 'mt_allow_pings': 1,
 'page_id': '2',
 'page_status': 'publish',
 'permaLink': 'http://192.168.50.70/index.php/start-page.html',
 'text_more': '',
 'title': '关于',
 'userid': '1',
 'wp_author': 'admin',
 'wp_author_display_name': 'admin',
 'wp_author_id': '1',
 'wp_page_order': '0',
 'wp_page_parent_id': '0',
 'wp_page_parent_title': '',
 'wp_page_template': '',
 'wp_password': '',
 'wp_slug': 'start-page'}

Get Pages
`````````
The page count is optional

>>> te.get_pages()
[{'categories': [],
  'custom_fields': [],
  'dateCreated': <DateTime '20200131T14:10:16' at 0x22e3d0152e0>,
  'date_created_gmt': <DateTime '20200131T06:10:16' at 0x22e3d015490>,
  'description': '<p>本页面由 Typecho 创建, 这只是个测试页面.</p>',
  'excerpt': '本页面由 Typecho 创建, 这只是个测试页面.',
  'link': 'http://192.168.50.70/index.php/start-page.html',
  'mt_allow_comments': 1,
  'mt_allow_pings': 1,
  'page_id': 2,
  'page_status': 'publish',
  'permaLink': 'http://192.168.50.70/index.php/start-page.html',
  'text_more': '',
  'title': '关于',
  'userid': '1',
  'wp_author': 'admin',
  'wp_author_display_name': 'admin',
  'wp_author_id': '1',
  'wp_page_order': 0,
  'wp_page_parent_id': 0,
  'wp_page_parent_title': '',
  'wp_page_template': '',
  'wp_password': '',
  'wp_slug': 'start-page'},
  ...
]

New Page
`````````
You should create a Page instance at first.

>>> page = Page(title='Page Title', description='Page Description')
>>> te.new_page(page, publish=True)
'4'

Edit Page
`````````
You should create a Page instance at first. And specific a page id(cid).

>>> page = Page(title='Edited Page Title', description='Edited Page Description')
>>> te.edit_page(page, page_id=3, publish=True)
'4'

Delete Page
````````````
A page id(cid) is required.

>>> te.del_page(4)
True

Category
------------------

Get Categories
```````````````
No argument.

>>> te.get_categories()
[{'categoryDescription': '只是一个默认分类',
  'categoryId': '1',
  'categoryName': '默认分类',
  'description': '默认分类',
  'htmlUrl': 'http://192.168.50.70/index.php/category/default/',
  'parentId': '0',
  'rssUrl': 'http://192.168.50.70/index.php/feed/category/default/'}
  ...
]

New Category
```````````````
You should create a Category instance at first.

>>> category = Category(name='Category Name')
>>> te.new_category(category)
'2'

Delete Category (NOT WORK!)
```````````````````````````
A category id(mid) is required.

>>> te.del_category(2)
True

Tag
------------------

Get Tags
```````````````
No argument.

>>> te.get_tags()
['A', 'B']

Attachment
------------------

Get Attachment
```````````````
A attachment cid is required.

>>> te.get_attachment(1)
{'attachment_id': '3',
 'caption': 'test-png',
 'date_created_gmt': <DateTime '20200226T21:35:41' at 0x1fc12bd4340>,
 'description': '',
 'link': 'http://127.0.0.1/usr/uploads/2020/02/965447938.png',
 'metadata': {'file': '/usr/uploads/2020/02/965447938.png', 'size': 1372},
 'parent': '0',
 'thumbnail': 'http://127.0.0.1/usr/uploads/2020/02/965447938.png',
 'title': 'test.png'}

Get Attachments
```````````````
The post id is optional

>>> te.get_attachments()
[{'attachment_id': '3',
  'caption': 'test-png',
  'date_created_gmt': <DateTime '20200226T21:39:55' at 0x216ef2343d0>,
  'description': '',
  'link': 'http://127.0.0.1/usr/uploads/2020/02/3499895551.png',
  'metadata': {'file': '/usr/uploads/2020/02/3499895551.png', 'size': 4093},
  'parent': '0',
  'thumbnail': 'http://127.0.0.1/usr/uploads/2020/02/3499895551.png',
  'title': 'test.png'},
  ...
]

New Attachment
```````````````
You should open a file at first.

>>> with open('resources/test.png', 'rb') as f:
>>> data = Attachment('test.png', f.read())
>>> te.new_attachment(data)
{'file': 'test.png',
 'url': 'http://127.0.0.1/usr/uploads/2020/02/3499895551.png'}

Comment
------------------

Get Comment (NOT WORK!)
````````````````````````
A comment id is required.

>>> te.get_comment(1)
None

Get Comments
````````````````````````
The post id is optional

>>> te.get_comments()
[{'author': 'Typecho',
  'author_email': '',
  'author_ip': '127.0.0.1',
  'author_url': 'http://typecho.org',
  'comment_id': '1',
  'content': '欢迎加入 Typecho 大家族',
  'date_created_gmt': <DateTime '20200131T14:10:16' at 0x23f0d1242e0>,
  'link': 'http://192.168.50.70/index.php/archives/1/#comment-1',
  'parent': '0',
  'post_id': '1',
  'post_title': '欢迎使用 Typecho',
  'status': 'approve',
  'type': 'comment',
  'user_id': '0'},
  ...
]

New Comment
````````````````````````
WARNING: Typecho Anti spam system default on! If you failed, please check you options.

>>> comment = Comment(author='admin', content='Comment')
>>> te.new_comment(comment, post_id=1)
2

Edit Comment
````````````````````````
WARNING: Typecho Anti spam system default on! If you failed, please check you options.

>>> comment = Comment(author='admin', content='Edited Comment')
>>> te.new_comment(comment, comment_id=2)
True

Delete Comment
````````````````````````
WARNING: Typecho Anti spam system default on! If you failed, please check you options.

>>> te.del_comment(comment_id=2)
True