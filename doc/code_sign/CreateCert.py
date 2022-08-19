# install with pip -> pyOpenSSL
from OpenSSL import crypto
import sys
import os

serialNumber = 00000
emailAddress = "your@email"
commonName = "nameOfCert"
countryName = "US"
localityName = "locality"
stateOrProvinceName = "stateOrProvince"
validityStartInSeconds = 0
validityEndInSeconds = 10*365*24*60*60

KEY_FILE = "CypressEnvironmentHelper.key"
CERT_FILE = "CypressEnvironmentHelper.crt"
CERT_DIR = os.path.dirname(sys.argv[0]) + "/certificate"


def cert_gen():
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 4096)
    cert = crypto.X509()

    cert.get_subject().C = countryName
    cert.get_subject().ST = stateOrProvinceName
    cert.get_subject().L = localityName
    cert.get_subject().CN = commonName
    cert.get_subject().emailAddress = emailAddress
    cert.set_serial_number(serialNumber)
    cert.gmtime_adj_notBefore(validityStartInSeconds)
    cert.gmtime_adj_notAfter(validityEndInSeconds)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha512')

    if not os.path.exists(CERT_DIR):
        os.mkdir(CERT_DIR)

    with open(f"{CERT_DIR}/{CERT_FILE}", "wt") as f:
        f.write(crypto.dump_certificate(
            crypto.FILETYPE_PEM, cert).decode("utf-8"))

    with open(f"{CERT_DIR}/{KEY_FILE}", "wt") as f:
        f.write(crypto.dump_privatekey(
            crypto.FILETYPE_PEM, key).decode("utf-8"))


cert_gen()
