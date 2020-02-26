from pytypecho import Category


def test_get_category(te):
    r = te.get_categories()
    assert r
    assert r[0]['categoryName'] == '默认分类'


def test_new_category(te):
    category = Category(name='Category Name')
    r = te.new_category(category)
    assert r
    assert r.isdigit()


def del_category(te):
    r = te.del_category(2)
    assert r
