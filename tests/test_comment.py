from pytypecho import Comment


def test_get_comment(te):
    r = te.get_comment(1)
    assert r
    assert r['author'] == 'Typecho'


def test_get_comments(te):
    r = te.get_comments()
    assert r
    assert r[0]['content'] == '欢迎加入 Typecho 大家族'
