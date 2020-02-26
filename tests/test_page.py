from pytypecho import Page


def test_get_page(te):
    r = te.get_page(2)
    assert r


def test_get_pages(te):
    r = te.get_pages()
    assert r


def test_new_page(te):
    page = Page(title='Page Title', description='Page Description')
    r = te.new_page(page, publish=True)
    assert r
    assert r.isdigit()


def test_edit_page(te):
    page = Page(title='Page Title', description='Page Description')
    num = te.new_page(page, publish=True)
    page_edited = Page(title='Edited Page Title', description='Edited Page Description')
    r = te.edit_page(page_edited, page_id=int(num), publish=True)
    assert r
    assert r == num


def test_del_post(te):
    page = Page(title='Del Page Title', description='Del Page Description')
    num = te.new_page(page, publish=True)
    r = te.del_page(int(num))
    assert r
