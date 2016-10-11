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


if __name__ == "__main__":
    google.run_me()
