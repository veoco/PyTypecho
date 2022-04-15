# PyTypecho

[![PyTypecho](https://github.com/veoco/PyTypecho/actions/workflows/python-ci.yml/badge.svg)](https://github.com/veoco/PyTypecho/actions/workflows/python-ci.yml)
[![Documentation Status](https://readthedocs.org/projects/pytypecho/badge/?version=latest)](https://pytypecho.readthedocs.io/en/latest/?badge=latest)

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

or

```python
import asyncio
from pytypecho import AsyncTypecho


async def main():
  te = AsyncTypecho('http://127.0.0.1/index.php/action/xmlrpc', username='admin', password='admin', semaphore=4)
  print(await te.get_posts())

asyncio.run(main())
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
  - [x] new Category (Not work on typecho >= 1.2)
  - [x] delete Category
- [x] Tag
  - [x] get Tags
- [x] Attachment
  - [x] get attachment/attachments
  - [x] new attachment
- [x] Comment
  - [x] get comment/comments
  - [x] new comment
  - [x] edit comment
  - [x] delete comment

### Others
- [x] Tests
- [x] Documentations

## License
PyTypecho is released under the MIT License. See LICENSE for more information.