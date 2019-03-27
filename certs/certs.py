from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
import datetime
import logging

def generate_ssl_certs(country, country_code, location, org, email, org_unit="NBIS sysdevs", common_name="NBIS"):
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    priv_key = key.private_bytes(encoding=serialization.Encoding.PEM,
                                format=serialization.PrivateFormat.TraditionalOpenSSL,
                                encryption_algorithm=serialization.NoEncryption(),)

    subject = issuer = x509.Name([x509.NameAttribute(NameOID.COUNTRY_NAME, country_code),
                                x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, country),
                                x509.NameAttribute(NameOID.LOCALITY_NAME, location),
                                x509.NameAttribute(NameOID.ORGANIZATION_NAME, org),
                                x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, org_unit),
                                x509.NameAttribute(NameOID.COMMON_NAME, common_name),
                                x509.NameAttribute(NameOID.EMAIL_ADDRESS, email), ])

    cert = x509.CertificateBuilder().subject_name(
        subject).issuer_name(
        issuer).public_key(
        key.public_key()).serial_number(
        x509.random_serial_number()).not_valid_before(
        datetime.datetime.utcnow()).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=1000)).add_extension(
        x509.SubjectAlternativeName([x509.DNSName(u"localhost")]), critical=False,).sign(
        key, hashes.SHA256(), default_backend())

    with open('certs' + '/' + 'ssl.cert', "w") as ssl_cert:
        ssl_cert.write(cert.public_bytes(serialization.Encoding.PEM).decode('utf-8'))

    with open('certs' + '/' + 'ssl.key', "w") as ssl_key:
        ssl_key.write(priv_key.decode('utf-8'))
