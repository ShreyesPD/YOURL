import traceback
import urllib.request
import urllib.parse
import hashlib


def generate_screenshot_api_url(customer_key, secret_phrase, options):
    try:
        api_url = 'https://api.screenshotmachine.com/?key=' + customer_key
        if secret_phrase:
            api_url = api_url + '&hash=' + hashlib.md5((options.get('url') + secret_phrase).encode('utf-8')).hexdigest()
        api_url = api_url + '&' + urllib.parse.urlencode(options)
        return api_url
    except Exception as e:
        print("ss exception occcured")
        traceback.print_exc()
        return ("0")

def preview(url):
    customer_key = '4ba519'
    secret_phrase = ''  # leave secret phrase empty, if not needed
    options = {
        'url': '',  # mandatory parameter
        # all next parameters are optional, see our website screenshot API guide for more details
        'dimension': '480x800',  # or "1366xfull" for full length screenshot
        'device': 'phone',
        'cacheLimit': '0',
        'delay': '200',
        'zoom': '100'
    }
    options['url'] = url
    api_url = generate_screenshot_api_url(customer_key, secret_phrase, options)

    # put link to your html code
    print('<img src="' + api_url + '">')
    return api_url
    # #or save screenshot as an image
    # opener = urllib.request.build_opener()
    # opener.addheaders = [('User-agent', '-')]
    # urllib.request.install_opener(opener)
    # output = 'output.png'
    # urllib.request.urlretrieve(api_url, output)
    # print('Screenshot saved as ' + output);
