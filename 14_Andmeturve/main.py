import pytest
import hashlib
import base64
import ssl
import requests

from urllib.parse import urljoin
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.x509 import ocsp
from cryptography.x509.ocsp import OCSPResponseStatus
from cryptography.x509.oid import ExtensionOID, AuthorityInformationAccessOID



def demo_liitja(a,b):
    '''
    Näidis, kuidas automaattestid töötavad.
    test_demos on kirjutatud testid, mille vastu funktsiooni kontrollitakse. Jooksuta test_demo erinevate tagastatavate
    väärtustega ja vaata kas testid ebaõnnestuvad.
    '''
    return a+b
    # return abs(a)+abs(b)
    # return a+b+1

# Ülesanne 1
def ülesanne1():
    '''
    Selles ülesandes on sinu ülesanne selline sisend, mille korral sisendile vastav SHA-256 räsi algab vähemalt nelja
    null bitiga ehk esimese baidi väärtus peab olema kuni 2**4 ehk 16.

    Funktsioon räsib sinu sisendi "räsitav" sha256 algorütmi järgi ning tagastab räsi.
    :return: räsitavale vastav SHA256 räsi
    '''
    räsitav = "sinu_sisend"
    räsi = hashlib.sha256(bytes(räsitav, "utf-8")).digest()
    # print(f"Proovisid sisendit '{räsitav}', mille räsi on {räsi}, algusega {räsi[0]}")
    return räsi


def Caesar_krüpteeri(avatekst: str, nihe: int):
    '''
    Caesari šiffer on üks tuntumaid asendusšifreid. Etteantud avateksti ja nihke alusel asendatakse kõik tähed avatekstis
    nihke võrra järgmise tähega. See tähendab, et kui sõna on aed ja nihe on 3, siis krüpteeritud sõna on dhg. Kui nihke
    tõttu läheks täht tähestikust välja, siis alustakse tähestiku algusest(nt öö, 4 puhul on tulemus aa).
    :param avatekst: Krüpteeritav tekst
    :param nihe: täisarv, mille võrra avateksti tähti tähestikus "edasi lükatakse".
    :return: salakiri
    '''
    avatekst_väike = avatekst.lower()
    tähestik = "abcdefghijklmnopqrsšzžtuvwõäöüxy"

    salakiri = ""
    for char in avatekst_väike:
        if char in tähestik:
            indeks = tähestik.index(char)
            salakiri += tähestik[(indeks + nihe) % len(tähestik)]
        else:
            salakiri += char
    return salakiri


# Paneme tähele, et kasutades negatiivset nihet on võimalik sama meetodiga ka dekrüpteerida.

def ülesanne2():
    '''Teie ülesanne on dekrüpteerida alljärgnev sõnum. On teada, et sõnum on krüpteeritud Caesari šifriga.
    wpavpxüubb äpaf üõu ššbxšašb wpöžšõpbšwb fjgbögs. fp üõšwb wpöžšõpbšwb fjgbögs wüžg hpažpäkšõ, 
    wgu üõšwb fšpfgs, wgbf bpu üag xšpag üäp wštpõš buöubšs õpužgs.
    '''
    vastus = "..."
    return vastus


########################################################################################
# Avaliku võtme krüptograafia ei taga, et teine osapool on tõesti see, kes ta väidab end olevat. Näiteks sotsiaalmeedias
# tagab krüptograafia, et ainult autoriseeritud inimene saab kontole ligi(parool/näotuvastus...),
# kuid miski ei takista pahalasel teha teisenimeline konto. Ehk George võib teha Bobi nimelise konto ning kui Alice
# soovib kirjutada Bobile privaatse sõnumi, siis võib ta pahaaimamatult saata selle valele Bobile ehk Georgele.

# Prakikas on probleemi lahendamiseks loodud avaliku võtme taristu(PKI) süsteem reaalse inimese ja tema avaliku võtme
# sidumiseks. Sisuliselt tähendab see, et on usaldatud teenusepakkujad, kes annavad sertifikaate, et inimene/veebileht
# tõesti omab vastavat avalikku võtit.

# Allpool on kood, millega saab Pythonis kontrollida veebilehtede sertifikaati. Samasugune funktsionaalsus on ka
# tänapäevastesse brauseritesse sisseehitatud(lukumärk, otsinguakna vasemas nurgas).

def leia_lehe_sertifikaat(leht, port):
    conn = ssl.create_connection((leht, port))
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    sock = context.wrap_socket(conn, server_hostname=leht)
    certDER = sock.getpeercert(True)
    certPEM = ssl.DER_cert_to_PEM_cert(certDER)
    return x509.load_pem_x509_certificate(certPEM.encode('ascii'), default_backend())


# Veebilehe sertifikaadis on ära täpsustatud, mis serfikaadiasutus on lehele sertifikaadi andnud. Meetod loeb selle
# lehe sertifikaadi AIA väljalt välja.
def leia_sertifikaadikeskus(cert):
    aia = cert.extensions.get_extension_for_oid(ExtensionOID.AUTHORITY_INFORMATION_ACCESS).value
    issuers = [ia for ia in aia if ia.access_method == AuthorityInformationAccessOID.CA_ISSUERS]
    if not issuers:
        raise Exception(f'Sertifikaadis ei ole väljaandjat täpsustatud')
    return issuers[0].access_location.value


# Veebilehe sertifikaadis on ära täpsustatud, kes pakub kinnitab, et lehele antud sertifikaat on endiselt kehtiv.
# Meetod loeb kinnitusepakkuja lehe sertifikaadi AIA väljalt välja.
def leia_kehtivuskinnituse_pakkuja(cert):
    aia = cert.extensions.get_extension_for_oid(ExtensionOID.AUTHORITY_INFORMATION_ACCESS).value
    ocsps = [ia for ia in aia if ia.access_method == AuthorityInformationAccessOID.OCSP]
    if not ocsps:
        raise Exception(f'no ocsp server entry in AIA')
    return ocsps[0].access_location.value


def leia_serfikaadikeskuse_sertifikaat(ca_issuer):
    issuer_response = requests.get(ca_issuer)
    if issuer_response.ok:
        issuerDER = issuer_response.content
        issuerPEM = ssl.DER_cert_to_PEM_cert(issuerDER)
        return x509.load_pem_x509_certificate(issuerPEM.encode('ascii'), default_backend())
    raise Exception(f'Sertifikaadikeskuse sertifikaadi leidmine ebaõnnestus: {issuer_response.status_code}')


def koosta_kehtivuskinnitusepäring(ocsp_server, cert, issuer_cert):
    builder = ocsp.OCSPRequestBuilder()
    builder = builder.add_certificate(cert, issuer_cert, SHA256())
    req = builder.build()
    req_path = base64.b64encode(req.public_bytes(serialization.Encoding.DER))
    return urljoin(ocsp_server + '/', req_path.decode('ascii'))


def kontrolli_kehtivuskinnitust(ocsp_server, cert, issuer_cert):
    ocsp_resp = requests.get(koosta_kehtivuskinnitusepäring(ocsp_server, cert, issuer_cert))
    if ocsp_resp.ok:
        ocsp_decoded = ocsp.load_der_ocsp_response(ocsp_resp.content)
        if ocsp_decoded.response_status == OCSPResponseStatus.SUCCESSFUL:
            return ocsp_decoded.certificate_status
        else:
            return ocsp_decoded.response_status
    return ocsp_resp.status_code


def sertifikaadi_staatus(leht, port=443):
    print('veebileht:', leht, "    port:", port)
    cert = leia_lehe_sertifikaat(leht, port)
    ca_issuer = leia_sertifikaadikeskus(cert)
    print('sertifitseerimisasutuse sertifikaat:', ca_issuer)
    issuer_cert = leia_serfikaadikeskuse_sertifikaat(ca_issuer)
    ocsp_server = leia_kehtivuskinnituse_pakkuja(cert)
    print('päring sertifikaadi ajakohasuse kohta lehelt:', ocsp_server)
    print("sertifikaadi_staatus: ", kontrolli_kehtivuskinnitust(ocsp_server, cert, issuer_cert))
    return kontrolli_kehtivuskinnitust(ocsp_server, cert, issuer_cert) == OCSPResponseStatus.SUCCESSFUL


def ülesanne3():
    return sertifikaadi_staatus('moodle.ut.ee')


###########################################################################################
# ülesanne4
# parooliräsid.txt sisaldab SHA256 räsisid, mis on saadud juhuslikkest tähtedest koosnevatest paroolidest pikkusega 2-8
# tähte. Lisaks juhuslikele paroolidele on seal 5 sagedasti kasutatud parooli räsid.
# Teie ülesanne on leida vähemalt 3 parooli, mille SHA256 räsi on antud failis.
# Vihje: Võid proovida lihtsalt erinevaid paroole, kuid võid ka mõelda/otsida internetist enam kasutatud paroolide nimekirja.
# Mitme tähe juures jookseb piir, kust arvuti ei suuda mõistliku ajaga kõiki variante läbiproovida?
def ülesanne4():
    paroolid = ["parool1",
                "parool2",
                "parool3"]
    räsid = []
    for parool in paroolid:
        räsid.append(proovi_parooli(parool))
    return räsid


# ülesanne5
# soolatud_parooliräsid.txt sisaldab SHA256 räsisid ja juhuslikult genereeritud 16 baidiseid soolasid esitatuna
#   kuueteistkümnendsüsteemis. Igal real failis on üks räsi ja sool ning nad on eraldatud semikooloniga.
# Räsid on tuletatud parooli ja soola konkatenatsioonist. parool+sool=paroolsool
# Teie ülesanne on leida 1 parool ja sool kombinatsioon, mille räsi on antud failis.
# Vihje: Võid proovida lihtsalt erinevaid paroole, kuid võid ka mõelda/otsida internetist enam kasutatud paroolide nimekirja.
# Mõtlemiseks: Kui soolad on avalikud ja krüpteerimata, siis kuidas tõstab see paroolide turvalisust.
def ülesanne5():
    parool = "K,"
    sool = bytes.fromhex("05c2247b961060a250bc364d55f10512")
    return proovi_parooli(parool, sool)


# abimeetod, mis kontrollib parooli sobivust.
def on_sobiv_parool(parool):
    if len(parool) > 16:
        raise Exception("Liiga pikk parool. Max pikkus on 16 märki")
    for täht in parool:
        if ord(täht) >= 128 and ord(täht) >= 32:
            raise Exception("Proovitav parool sisaldab tundmatuid tähte.", täht)
    return True


# abimeetod, mis tagastab soola ja paroolile vastava räsi
def proovi_parooli(parool: str, sool: bytes = b""):
    if on_sobiv_parool(parool):
        räsi = hashlib.sha256(bytes(parool, "ascii") + sool).digest().hex()
    return räsi


'''
Kood, mille alusel parooliräsid ja soolad genereertud
passwords = []
with open("abifailid/paroolid.txt") as f:
    for row in f:
        passwords.append(row.strip())

with open("abifailid/parooliräsid.txt", "w") as f:
    for pw in passwords:
        f.write(hashlib.sha256(bytes(pw, "ascii")).digest().hex())
        f.write("\n")

passwords = []
with open("abifailid/paroolid2.txt") as f:
    for row in f:
        passwords.append(row.strip())

with open("abifailid/soolatud_parooliräsid.txt", "w") as f:
    for pw in passwords:
        salt = os.urandom(16)
        f.write(hashlib.sha256(bytes(pw, "ascii") + salt).digest().hex())
        f.write(";")
        f.write(salt.hex())
        f.write("\n")
'''
pytest.main()
