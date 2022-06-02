from scripts.reverse_string import reverse_string


def test_reverse_two_char_string():
    assert reverse_string("lo") == "ol"


def test_reverse_long_string():
    assert reverse_string("abcdefg") == "gfedcba"
