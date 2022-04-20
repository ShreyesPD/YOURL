import whois


def domain_info(url):
    w = whois.whois(url)
    # print(w.expiration_date)  # dates converted to datetime object datetime.datetime(2013, 6, 26, 0, 0)
    # print(w.text)
    return (w.text)

