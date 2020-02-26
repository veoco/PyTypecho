from pytypecho import Post


def test_get_post(te):
    r = te.get_post(1)
    assert r


def test_get_posts(te):
    r = te.get_posts()
    assert r


def test_new_post(te):
    post = Post(title='Post Title', description='Post Description')
    r = te.new_post(post, publish=True)
    assert r
    assert r.isdigit()


def test_edit_post(te):
    post = Post(title='Post Title', description='Post Description')
    num = te.new_post(post, publish=True)
    post_edited = Post(title='Edited Post Title', description='Edited Post Description')
    r = te.edit_post(post_edited, post_id=int(num), publish=True)
    assert r
    assert r == num


def test_del_post(te):
    post = Post(title='Del Post Title', description='Del Post Description')
    num = te.new_post(post, publish=True)
    r = te.del_post(int(num))
    assert r is None
