import math
import random
import hashlib


def on_algarv(a):
  for i in range(2, int(math.sqrt(a))+1):
    if a%i==0: return False
  return True

def genereeri_algarv(bitid):
  arv = int(random.randint(2**(bitid-1), 2**bitid))
  while True:
    if on_algarv(arv):
      return arv
    arv+=1

def süt(x, y):
  while y != 0:
    (x, y) = (y, x % y)
  return x

def leia_lcm (a, b):
  return a*b//süt(a,b)

def lsüt(a, b):
  if a == 0:
    return (b, 0, 1)
  else:
    g, y, x = lsüt(b % a, a)
    return (g, x - (b // a) * y, y)

def leia_e(a):
  for i in range(2, int(math.sqrt(a))+1):
    if a%i!=0 and on_algarv(i): return i
  raise Exception("Given a does not have a coprime.")



def pöördmoodul(lcm, m):
    g, x, y = lsüt(lcm, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def genereeri_võtmed(bitid):
  p = genereeri_algarv(bitid//2)
  q = genereeri_algarv(bitid//2)
  n = p*q
  lcm = leia_lcm(p-1, q-1)
  e = leia_e((p-1)*(q-1))
  d = pöördmoodul(e, lcm)
  return (p,q,n,lcm,e,d)


def enc ( m, n, e ) :
  #return m**e % n
  #Päris palju efektiivsem alternatiiv
  return pow(m, e, n)

def allkirjasta_sõnum(sõnum, privaatne_võti, räsifunk=hashlib.sha256):
  #Räsime sõnumi ära
  m = räsifunk()
  m.update(bytes(sõnum, "utf-8"))
  räsi = m.digest()

  #Teeme räsist arvu
  räsi_arv = int.from_bytes(räsi, "big")

  #Krüpteerime räsist tekitatud arvu
  allkirjastatud_sõnum = enc(räsi_arv, privaatne_võti[0], privaatne_võti[1])
  pakk = (allkirjastatud_sõnum, sõnum, räsifunk)
  return pakk

def kontrolli_allkirja(pakk, avalik_võti, räsifunk=hashlib.sha256):
  #Räsime olulise sõnumi ära
  m = räsifunk()
  m.update(bytes(pakk[1], "utf-8"))
  räsi = m.digest()

  #Teeme räsist arvu. Sellega võrdleme allkirjastud arvule vastavat räsi.
  räsi_arv = int.from_bytes(räsi, "big")

  #Leiame allkirjastud räsiarvust räsi
  allkirjastatud_sõnumi_räsi_arv = enc(pakk[0], avalik_võti[0], avalik_võti[1])
  allkirjastatud_sõnumi_räsi = allkirjastatud_sõnumi_räsi_arv.to_bytes((
      allkirjastatud_sõnumi_räsi_arv.bit_length()+7)//8, "big")