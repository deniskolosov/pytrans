
DICTIONARIES = {'en_ru':
                {'hello': 'привет',
                 'world': 'мир'}}


def translate(translate_from, translate_to, string_to_translate=""):
    """
    Translate plugin with rather limited dictionary, for the moment the only words it can translate are 'hello'
    and 'world'.

    :param translate_from: language to translate from
    :param translate_to: language to translate to
    :param string_to_translate: text to translate
    :return:
    """
    dictionary = DICTIONARIES.get("%s_%s" % (translate_from, translate_to))
    if not dictionary:
        print("Offline: No such translation direction in dictionary: %s-%s" % (translate_from, translate_to))
    else:
        words = [dictionary.get(w, w) for w in string_to_translate.split(' ')]
        print("Offline: %s" % (' '.join(words)))

