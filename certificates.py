# """# import requests module
# import requests
#
# # Making a get request
# response = requests.get('https://expired.badssl.com/')
#
# # print request object
# print(response)
# """
#
#
# # -*- encoding: utf-8 -*-
# # requires a recent enough python with idna support in socket
# # pyopenssl, cryptography and idna
#
# from OpenSSL import SSL
# from cryptography import x509
# from cryptography.x509.oid import NameOID
# import idna
#
# from socket import socket
# from collections import namedtuple
#
# HostInfo = namedtuple(field_names='cert hostname peername', typename='HostInfo')
#
# HOSTS = [
#     ('damjan.softver.org.mk', 443),
#     ('expired.badssl.com', 443),
#     ('wrong.host.badssl.com', 443),
#     ('ca.ocsr.nl', 443),
#     ('faß.de', 443),
#     ('самодеј.мкд', 443),
# ]
#
# def verify_cert(cert, hostname):
#     # verify notAfter/notBefore, CA trusted, servername/sni/hostname
#     cert.has_expired()
#     # service_identity.pyopenssl.verify_hostname(client_ssl, hostname)
#     # issuer
#
# def get_certificate(hostname, port):
#     hostname_idna = idna.encode(hostname)
#     sock = socket()
#
#     sock.connect((hostname, port))
#     peername = sock.getpeername()
#     ctx = SSL.Context(SSL.SSLv23_METHOD) # most compatible
#     ctx.check_hostname = False
#     ctx.verify_mode = SSL.VERIFY_NONE
#
#     sock_ssl = SSL.Connection(ctx, sock)
#     sock_ssl.set_connect_state()
#     sock_ssl.set_tlsext_host_name(hostname_idna)
#     sock_ssl.do_handshake()
#     cert = sock_ssl.get_peer_certificate()
#     crypto_cert = cert.to_cryptography()
#     sock_ssl.close()
#     sock.close()
#
#     return HostInfo(cert=crypto_cert, peername=peername, hostname=hostname)
#
# def get_alt_names(cert):
#     try:
#         ext = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName)
#         return ext.value.get_values_for_type(x509.DNSName)
#     except x509.ExtensionNotFound:
#         return None
#
# def get_common_name(cert):
#     try:
#         names = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
#         return names[0].value
#     except x509.ExtensionNotFound:
#         return None
#
# def get_issuer(cert):
#     try:
#         names = cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)
#         return names[0].value
#     except x509.ExtensionNotFound:
#         return None
#
#
# def print_basic_info(hostinfo):
#     s = '''» {hostname} « … {peername}
#     \tcommonName: {commonname}
#     \tSAN: {SAN}
#     \tissuer: {issuer}
#     \tnotBefore: {notbefore}
#     \tnotAfter:  {notafter}
#     '''.format(
#             hostname=hostinfo.hostname,
#             peername=hostinfo.peername,
#             commonname=get_common_name(hostinfo.cert),
#             SAN=get_alt_names(hostinfo.cert),
#             issuer=get_issuer(hostinfo.cert),
#             notbefore=hostinfo.cert.not_valid_before,
#             notafter=hostinfo.cert.not_valid_after
#     )
#     print(s)
#
# def check_it_out(hostname, port):
#     hostinfo = get_certificate(hostname, port)
#     print_basic_info(hostinfo)
#
#
# import concurrent.futures
# if __name__ == '__main__':
#     with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:
#         for hostinfo in e.map(lambda x: get_certificate(x[0], x[1]), HOSTS):
#             print_basic_info(hostinfo)
#
#
#
# '''import urllib.request
# request_url = urllib.request.urlopen('https://www.geeksforgeeks.org/')
# print(request_url.read())
# '''
#
# '''from urllib.parse import *
# parse_url = urlparse('https://www.sslshopper.com/ssl-checker.html#hostname=facebook.com')
# print(parse_url)
# print("\n")
# unparse_url = urlunparse(parse_url)
# print(unparse_url)
# '''
#
# '''import socket
# IP_addres = socket.gethostbyname('www.sslshopper.com')
# print("IP Address is:" + IP_addres)
# '''
#
# '''
# import requests
# strn='http://'
# print(help(requests.get(strn+'barc.gov.in')))
# '''
# '''
# import ssl,OpenSSL
# cert = ssl.get_server_certificate(('www.google.com', 443))
# #print(cert)
# x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
# print(x509.get_subject().get_components())
# print(x509.get_subject().as_text())
# #x509 = M2Crypto.X509.load_cert_string(cert)
# #print(x509.get_subject().as_text())
# '''
#
# '''
# import ssl
# import socket
# import OpenSSL
# from pprint import pprint
# from datetime import datetime
#
#
# def get_certificate(host, port=443, timeout=10):
#     context = ssl.create_default_context()
#     conn = socket.create_connection((host, port))
#     sock = context.wrap_socket(conn, server_hostname=host)
#     sock.settimeout(timeout)
#     try:
#         der_cert = sock.getpeercert(True)
#     finally:
#         sock.close()
#     return ssl.DER_cert_to_PEM_cert(der_cert)
#
#
# certificate = get_certificate('gcq.ac.in')
# x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, certificate)
#
# result = {
#     'subject': dict(x509.get_subject().get_components()),
#     'issuer': dict(x509.get_issuer().get_components()),
#     'serialNumber': x509.get_serial_number(),
#     'version': x509.get_version(),
#     'notBefore': datetime.strptime(x509.get_notBefore().decode('UTF-8'), '%Y%m%d%H%M%SZ'),
#     'notAfter': datetime.strptime(x509.get_notAfter().decode('UTF-8'), '%Y%m%d%H%M%SZ')
# }
#
# extensions = (x509.get_extension(i) for i in range(x509.get_extension_count()))
# extension_data = {e.get_short_name(): str(e) for e in extensions}
# result.update(extension_data)
# pprint(result)
# '''

import socket
import ssl
import datetime

"""domains_url = [
"devnote.in",
"devnote_wrong.in",
"stackoverflow.com",
"stackoverflow.com/status/404"
]"""

#domains_url=["gcq.ac.in"]

def ssl_expiry_datetime(hostname):
    try:
        ssl_dateformat = r'%b %d %H:%M:%S %Y %Z'

        context = ssl.create_default_context()
        context.check_hostname = False

        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=hostname,
        )
        # 5 second timeout
        conn.settimeout(5.0)

        conn.connect((hostname, 443))
        ssl_info = conn.getpeercert()
        # Python datetime object

        now = datetime.datetime.now()
        expire = datetime.datetime.strptime(ssl_info['notAfter'], ssl_dateformat)
        diff = expire - now
        return ("Domain name: {} Expiry Date: {} Expiry Day: {}".format(hostname,expire.strftime("%Y-%m-%d"),diff.days))
    except Exception as e:
        return (e)
#ssl_expiry_datetime("gcq.ac.in")
