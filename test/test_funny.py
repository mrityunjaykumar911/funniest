from nose import with_setup


def test_b():
    import funniest
    assert funniest.joke() == "ek haathi tha, ek chiti thi" + "ek din chiti ne kaha" + "haahaa"
