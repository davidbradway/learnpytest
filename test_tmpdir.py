# content of test_tmpdir.py
def test_needsfiles(tmpdir):
    print (tmpdir)
    assert tmpdir.check()
