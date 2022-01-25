from importlib import import_module
yl = import_module('14_Andmeturve.main')


def test_neliEsimestNulli():
    assert yl.ülesanne1()[0] <= 16