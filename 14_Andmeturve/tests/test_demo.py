from importlib import import_module
yl = import_module('14_Andmeturve.main')


def test_demo_positiivsed_arvud():
    assert yl.demo_liitja(4, 5) == 9

def test_demo_negatiivsed_arvud():
    assert yl.demo_liitja(-2, -3) == -5