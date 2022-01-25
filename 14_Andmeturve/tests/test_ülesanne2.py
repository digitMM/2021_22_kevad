from importlib import import_module
import hashlib
yl = import_module('14_Andmeturve.main')


def test_dekrüpteerimine():
    assert hashlib.sha256(bytes(yl.ülesanne2(), "utf-8")).digest() == b"]o\xc8z]\x97\xb1\x1d\x12\xce\xbb\\{\xcfrr\xcc,js\xb6Lm\xa2\xd4\xdc\xa9\xa0'E|K"
