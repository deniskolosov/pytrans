
DICTIONARIES = {'en_ru':
                {'hello': 'привет',
                 'world': 'мир'}}


def translate(translate_from, translate_to, string_to_translate=""):
    dictionary = DICTIONARIES.get("%s_%s" % (translate_from, translate_to))
    words = [dictionary.get(w, w) for w in string_to_translate.split(' ')]
    print("Offline: %s" % (' '.join(words)))

if __name__ == "__main__":
    translate("en", "ru", "hello world")