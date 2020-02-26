def test_get_attachments(te):
    r = te.get_attachments()
    assert r == []
