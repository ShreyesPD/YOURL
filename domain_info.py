import traceback

import whois


# def domain_info(url):
#     w = whois.whois(url)
#     # print(w.expiration_date)  # dates converted to datetime object datetime.datetime(2013, 6, 26, 0, 0)
#     # print(w.text)
#     return (w.text)

#domain_info("facebook.com")

def domain_info(url):
    try:
        w = whois.whois(url)
        # print(w.expiration_date)  # dates converted to datetime object datetime.datetime(2013, 6, 26, 0, 0)
        #print(w.text.split("\n"))
        test_list = w.text.split("\n")
        remove_list = ["For more information on Whois status codes, please visit https://icann.org/epp\r", "NOTICE: The expiration date displayed in this record is the date the\r", "registrar's sponsorship of the domain name registration in the registry is\r", "currently set to expire. This date does not necessarily reflect the expiration\n", "date of the domain name registrant's agreement with the sponsoring\r", "registrar.  Users may consult the sponsoring registrar's Whois database to\r", "view the registrar's reported date of expiration for this registration.\r","TERMS OF USE: The information in the Whois database is collected through ICANN-accredited registrars. Jiangsu bangning science & technology Co., Ltd(“BANGNING”) make this information available to you and do not guarantee its accuracy or completeness. By submitting a whois query, you agree to abide by the following terms of use: you agree that you may use this data only for lawful purposes and that under no circumstances will you use this data to:  (1) to allow， enable， or otherwise support the transmission of mass unsolicited， commercial advertising or solicitations via direct mail， electronic mail， or by telephone; (2) in contravention of any applicable data and privacy protection acts; or (3) to enable high volume， automated， electronic processes that apply to BANGNING (or its computer systems). Compilation， repackaging， dissemination， or other use of the WHOIS database in its entirety， or of a substantial portion thereof， is not allowed without BANGNING prior written permission. You agree not to use electronic processes that are automated and high-volume to access or query the whois database except as reasonably necessary to register domain names or modify existing registrations. BANGNING reserves the right to restrict your access to the whois database in its sole discretion to ensure operational stability.  BANGNING may restrict or terminate your access to the whois database for failure to abide by these terms of use. BANGNING reserves the right to modify these terms at any time without prior or subsequent notification of any kind. \r", "For more information on Whois status codes, please visit https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en\r"]
        temp = [i for i in test_list if i not in remove_list]
        # str1 = ""
        # i = 0
        # # traverse in the string
        # print(type(temp))
        # for  ele in temp:
        #     print(ele)
        #     str1 = str1 + ele
        #     print(str1)
        #     i+=1
        #     print(i)

        str1 = ""

        # traverse in the string
        for ele in temp:
            str1 += ele

        return w.text

    except Exception as e:
        print(type(e).__name__)
        print("domain_info exception occcured")
        traceback.print_exc()
        return (url + "\n UNREGISTERED DOMAIN \n The above domain is available for purchase as it was never owned before or the previous ownership expired")
#print(domain_info("dramalongitude.top"))