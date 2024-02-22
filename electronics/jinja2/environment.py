from jinja2 import Environment, PackageLoader

from templatetags.basic_filter import getattribute


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            "getattribute": getattribute,  # Adding the macro to the global environment
        }
    )
    return env
