def test_get_posts(te):
    r = te.get_posts()
    assert r
    assert r[0]['title'] == '欢迎使用 Typecho'
