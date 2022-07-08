# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import traceback

import requests

# from bs4 import BeautifulSoup as soup

'''def testAPI:
    print('Enter IP Address:')
    ip_add = input()
    print('Enter The API key:')
    api_key = input()
    req = requests.get("https://www.virustotal.com/api/v3/ip_addresses/%s" %ip_add , headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0','x-apikey': '%s' % api_key}).json()
    dict_web = r["data"]["attributes"]["last_analysis_results"]
    tot_engine_c = 0
    tot_detect_c = 0
    result_eng = []
    eng_name = []
    count_harmless = 0
    for i in dict_web:
        tot_engine_c = 1 + tot_engine_c
        if dict_web[i]["category"] == "malicious" or dict_web[i]["category"] == "suspicious":
            result_eng.append(dict_web[i]["result"])
            eng_name.append(dict_web[i]["engine_name"])
            tot_detect_c = 1 + tot_detect_c
    res = []
    for i in result_eng:
        if i not in res:
            res.append(i)
    result_eng = res
    if tot_detect_c > 0:
        print("The %s was rated for" % ip_add + str(result_eng)[1:-1] + " on" + str(tot_detect_c) + " engines out of " + str(tot_engine_c) + " engines. The Engines which reported this are: " + str(eng_name)[1:-1] + ".")
    else:
        print("The IP %s " %ip_add + "has been marked harmless and clean on virustotal")
    
# Press the green button in the gutter to run the script.'''

# import time
import json


# import pandas

def testAPI(Urls):
    try:
        # file_path = str(input('please Enter The File Path: '))
        # domain_CSV = pandas.read_csv((file_path))

        # Urls = domain_CSV['Domain'].tolist()


        API_key = '5f79c5add1dcdecc0c6271053237264900adb1feaa53588d7a54515095e8ca42'
        url = 'https://www.virustotal.com/vtapi/v2/url/report'

        parameters = {'apikey': API_key, 'resource': Urls}

        response = requests.get(url=url, params=parameters)
        json_response = json.loads(response.text)

        if json_response['response_code'] <= 0:
            return 'URL NOT FOUND'
        elif json_response['response_code'] >= 1:

            if json_response['positives'] <= 0:
                return 'CLEAN URL'
            else:
                return 'FLAGGED DANGEROUS'
    except Exception as e:
        print("api exception occcured")
        traceback.print_exc()
        return("api exception occcured")

    # time.sleep(15)


'''if __name__ == '__main__':
    #print_hi('PyCharm')
    testAPI()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''
