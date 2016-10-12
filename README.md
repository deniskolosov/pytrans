# pytrans
Cli translator with plugins built using python

#### Installation:
``` bash
$ git clone https://github.com/thefivekey/pytrans.git
$ cd pytrans/
$ pip install -r requirements.txt
```

#### Usage:
``` bash
$ python translate.py --from de --to ru 'hallo welt'
Google:  Привет мир
```

default plugin is first in 'plugins' directory. You can also specify 
a plugin, languages to translate, etc. More info is available by -h
command:
``` bash
$ python translate.py -h
usage: translate.py [-h] [--verbose] [--from TRANSLATE_FROM]
                    [--to TRANSLATE_TO]
                    text_to_translate [{google,offline,yandex}]

Translator app with plugins.

positional arguments:
  text_to_translate     Some text to translate (don't forget to quote it)
  {google,offline,yandex}
                        Name of translation plugin

optional arguments:
  -h, --help            show this help message and exit
  --verbose             Displays results from all plugins.
  --from TRANSLATE_FROM
                        Language to translate from
  --to TRANSLATE_TO     Language to translate to
```


#### Plugins:
To create a plugin, simply create a python file inside 'plugins' folder
with 'translate' function which has following signature: 
``` python
translate(translate_from, translate_to, string_to_translate="")
```
It should print results of translation to stdout.