# import socket
# import ssl
# import datetime
# import traceback
#
# def ssl_expiry_datetime(hostname):
#     try:
#         ssl_dateformat = r'%b %d %H:%M:%S %Y %Z'
#
#         context = ssl.create_default_context()
#         context.check_hostname = False
#
#         conn = context.wrap_socket(
#             socket.socket(socket.AF_INET),
#             server_hostname=hostname,
#         )
#         # 5 second timeout
#         conn.settimeout(5.0)
#
#         conn.connect((hostname, 443))
#         ssl_info = conn.getpeercert()
#         # Python datetime object
#
#         now = datetime.datetime.now()
#         expire = datetime.datetime.strptime(ssl_info['notAfter'], ssl_dateformat)
#         diff = expire - now
#         return ("Domain name: {} Expiry Date: {} Expiry Day: {}".format(hostname,expire.strftime("%Y-%m-%d"),diff.days))
#     except Exception as e:
#         print("certificate exception occcured")
#         traceback.print_exc()
#         return ("certificate exception occured")
# #ssl_expiry_datetime("gcq.ac.in")

import ssl, socket
import traceback


def ssl_info(hostname):
    try:
        #hostname = 'stackoverflow.com'
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((hostname, 443))
            cert = s.getpeercert()

        # subject= dict(x[0] for x in cert['subject'])
        # issued_to_common_name = subject['commonName']
        #
        # issuer = dict(x[0] for x in cert['issuer'])
        # issued_by_common_name = issuer['commonName']
        # issued_by_org_name = issuer['organizationName']
        # issued_by_count_name = issuer['countryName']
        #
        # issued_on = cert['notBefore']
        # expires_on = cert['notAfter']
        #
        # #print(type(issued_to))
        # #print(type(issuer))
        # #print(type(issued_by))
        #
        # print("isuued to:\n Common Name(CN) "+issued_to_common_name)
        #
        # #print(issuer)
        # print("issued by:\n Common Name(CN):"+issued_by_common_name)
        # print("Organisation Name: "+issued_by_org_name)
        # print("Country Name: "+issued_by_count_name)
        # #print(subject)
        #
        # print("issued on: "+issued_on)
        # print("expires_on: "+expires_on)
        # #print(type(cert))
        # #print(cert)

        return  (cert)
    except Exception as e:
        print("certificate exception occured: ")
        traceback.print_exc()
        return (0)