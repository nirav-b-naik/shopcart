from jinja2 import Environment

from electronics.templatetags.basic_filter import getattribute


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            "getattribute": getattribute,
        }
    )
    return env
