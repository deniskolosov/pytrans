import codecs

import requests

API_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

# protect from github key parsers, not for production :)
API_KEY = codecs.decode('geafy.1.1.20161011G203649M.qs1r780sp584r220.q25025oo53744571o0nns533rsn8n862546s5n1r',
                        'rot_13')


def translate(translate_from, translate_to, string_to_translate=""):
    params = {'key': API_KEY,
              'text': string_to_translate,
              'lang': '%s-%s' % (translate_from, translate_to)}

    response = requests.get(API_URL, params)

    try:
        result = response.json()
    except ValueError:
        print("Yandex: service request error: failed to decode json")
        return

    if str(result['code']) == '200':
        print("Yandex: ", result['text'])
    else:
        print("Yandex: request error, message: %s" % result['message'])
