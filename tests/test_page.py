def test_get_pages(te):
    r = te.get_pages()
    assert r
    assert r[0]['title'] == '关于'
