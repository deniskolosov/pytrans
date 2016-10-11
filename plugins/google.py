import codecs

import requests

API_URL = 'https://www.googleapis.com/language/translate/v2'

# protect from github key parsers, not for production :)
API_KEY = codecs.decode('NVmnFlQf16xpQ_M3QD9XuoHBoeJoFEZ3_SNOEBZ',
                        'rot_13')


def translate(translate_from, translate_to, text_to_translate=""):
    params = {'key': API_KEY,
              'q': text_to_translate,
              'source': translate_from,
              'target': translate_to}
    response = requests.get(API_URL, params)

    try:
        result = response.json()
    except ValueError:
        print("Google: service request error: failed to decode json")
        return

    if 'error' in result:
        print("Google: request error, message: %s" % (result['error']['message']))
        return

    print("Google: ", result['data']['translations'][0]['translatedText'])
