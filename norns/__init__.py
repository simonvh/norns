import norns.cfg

from norns.exceptions import ConfigError


def config(name=None, config_file=None, default=None):
    return norns.cfg.Config(name=name, config_file=config_file, default=default)
