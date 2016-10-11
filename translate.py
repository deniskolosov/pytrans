import argparse
import os
from functools import partial

from pluginbase import PluginBase


# For easier usage calculate the path relative to here.
here = os.path.abspath(os.path.dirname(__file__))
get_path = partial(os.path.join, here)

plugin_base = PluginBase(package='translate.plugins')
plugin_source = plugin_base.make_plugin_source(searchpath=[get_path('./plugins')])

with plugin_source:
    from translate.plugins import google

parser = argparse.ArgumentParser(description="Translator app with plugins.")

parser.add_argument("string_to_translate", help="Some text to translate (don't forget to quote it)")
parser.add_argument("--source", help="Language to translate from")
parser.add_argument("--to", help="Language to translate to")


if __name__ == "__main__":
    args = parser.parse_args()
    google.print_me(args.source, args.to, args.string_to_translate)
