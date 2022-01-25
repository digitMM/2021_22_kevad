from importlib import import_module
import hashlib
import os
yl = import_module('14_Andmeturve.main')


def test_paroolid():
    hashes=[]
    with open("abifailid/soolatud_parooliräsid.txt") as f:
        for line in f:
            if yl.ülesanne5() == line.split(";")[0]:
                return
    raise Exception("Sain räsi:", yl.ülesanne5(), ", mida ei ole failis soolatud_parooliräsid")
