def test_get_category(te):
    r = te.get_categories()
    assert r
    assert r[0]['categoryName'] == '默认分类'
