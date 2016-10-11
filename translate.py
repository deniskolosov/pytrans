import argparse
import os
from functools import partial

from pluginbase import PluginBase


# For easier usage calculate the path relative to here.
here = os.path.abspath(os.path.dirname(__file__))
get_path = partial(os.path.join, here)

plugin_base = PluginBase(package='translate.plugins')
plugin_source = plugin_base.make_plugin_source(searchpath=[get_path('./plugins')])

parser = argparse.ArgumentParser(description="Translator app with plugins.")

parser.add_argument("string_to_translate", help="Some text to translate (don't forget to quote it)")
parser.add_argument("--from", dest="translate_from", help="Language to translate from")
parser.add_argument("--to", dest="translate_to", help="Language to translate to")


if __name__ == "__main__":
    args = parser.parse_args()

    for plugin_name in plugin_source.list_plugins():
        plugin = plugin_source.load_plugin(plugin_name)
        plugin.translate(args.translate_from, args.translate_to, args.string_to_translate)
