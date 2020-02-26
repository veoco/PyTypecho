# PyTypecho
Python Typecho Client (XMLRPC).

## Introduction

### Requirements
- Python >= 3.7

### Install 
```bash
pip install pytypecho
```

### Usage
```python
from pytypecho import Typecho


te = Typecho('http://127.0.0.1/index.php/action/xmlrpc', username='admin', password='admin')
print(te.get_posts())
```

### Documents
[ReadTheDocs](https://pytypecho.readthedocs.io/en/latest/)

## Status

### Functions
- [x] Post
  - [x] get Post/Posts
  - [x] new Post (Not fully tested!)
  - [x] edit Post
  - [x] delete Post
- [x] Page
  - [x] get Page/Pages
  - [x] new Page (Not fully tested!)
  - [x] edit Page
  - [x] delete Page
- [x] Category
  - [x] get Categories
  - [x] new Category
  - [x] delete Category(Not work)
- [x] Tag
  - [x] get Tags
- [x] Attachment
  - [x] get attachment/attachments
  - [x] new attachment
- [x] Comment
  - [x] get comment(Not work)/comments
  - [x] new comment
  - [x] edit comment
  - [x] delete comment

### Others
- [x] Tests
- [x] Documentations

## License
PyTypecho is released under the MIT License. See LICENSE for more information.