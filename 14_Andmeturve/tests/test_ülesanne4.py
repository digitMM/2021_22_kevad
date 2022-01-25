from importlib import import_module
import hashlib
yl = import_module('14_Andmeturve.main')


def test_paroolid():
    sobivad = []
    with open("abifailid/parooliräsid.txt") as f:
        for line in f:
            for räsi in set(yl.ülesanne4()):
                if räsi == line.strip():
                    sobivad.append(räsi)
    if len(sobivad) >= 3:
        return
    raise Exception(f"Sain ainult {len(sobivad)} sobivat räsi: {sobivad}.")


