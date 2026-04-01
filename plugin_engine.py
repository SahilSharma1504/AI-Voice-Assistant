plugins = {}


def register_plugin(name, function):

    plugins[name] = function


def run_plugin(name, command):

    if name in plugins:
        return plugins[name](command)

    return None