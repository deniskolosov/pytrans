import argparse
import inspect
import os
from functools import partial
from threading import Thread

import sys
from pluginbase import PluginBase


def _load_and_validate_plugin(plugin_name, plugin_source):
    """
    Validate and load plug from plugin source.
    :param plugin_name: name of plugin to load
    :param plugin_source: plugin source object
    :return: valid plugin object or None
    """
    plugin = plugin_source.load_plugin(plugin_name)

    # check if plugin has 'translate' function and it accepts 3 arguments
    has_translate = any([name == 'translate' for name, obj in inspect.getmembers(plugin, inspect.isfunction)])
    if not has_translate or len(inspect.signature(plugin.translate).parameters) != 3:
        print("Plugin error: '%s' doesn't have function translate or it doesn't accept 3 arguments needed"
              % plugin_name)
        return None
    return plugin


def run():
    parser = argparse.ArgumentParser(description="Translator app with plugins.")

    # For easier usage calculate the path relative to here.
    here = os.path.abspath(os.path.dirname(__file__))
    get_path = partial(os.path.join, here)

    plugin_base = PluginBase(package='translate.plugins')
    plugin_source = plugin_base.make_plugin_source(searchpath=[get_path('./plugins')])
    plugin_list = plugin_source.list_plugins()

    parser.add_argument("--verbose", help="Displays results from all plugins.", action="store_true")
    parser.add_argument("--from", dest="translate_from", help="Language to translate from", default='en')
    parser.add_argument("--to", dest="translate_to", help="Language to translate to", default='ru')
    parser.add_argument("text_to_translate", help="Some text to translate (don't forget to quote it)")
    parser.add_argument("plugin_name", help="Name of translation plugin", choices=plugin_list, nargs='?', type=str)

    args = parser.parse_args()

    thread_list = []

    if not plugin_list:
        print("Please, provide some plugins")
        sys.exit(0)

    plugin_name = args.plugin_name if args.plugin_name else plugin_list[0]

    if plugin_name and not args.verbose:
        plugin = _load_and_validate_plugin(plugin_name, plugin_source)
        if plugin:
            plugin.translate(args.translate_from, args.translate_to, args.text_to_translate)

    else:
        for name in plugin_list:
            plugin = _load_and_validate_plugin(name, plugin_source)

            if not plugin:
                continue

            t = Thread(target=plugin.translate, args=(args.translate_from, args.translate_to, args.text_to_translate,))
            t.start()
            thread_list.append(t)

        for t in thread_list:
            t.join()


if __name__ == "__main__":
    run()
