from pytypecho import Attachment


def test_get_attachments(te):
    with open('resources/test.png', 'rb') as f:
        data = Attachment('test.png', f.read())
        te.new_attachment(data)
        r = te.get_attachments()
        assert r


def test_get_attachment(te):
    with open('resources/test.png', 'rb') as f:
        data = Attachment('test.png', f.read())
        te.new_attachment(data)
        r = te.get_attachment(3)
        assert r


def test_new_attachment(te):
    with open('resources/test.png', 'rb') as f:
        data = Attachment('test.png', f.read())
        r = te.new_attachment(data)
        assert r['file'] == 'test.png'
