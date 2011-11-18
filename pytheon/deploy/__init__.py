# -*- coding: utf-8 -*-
from pytheon.utils import Config
from pytheon.utils import log
from pytheon import utils
from os.path import join
import os

__all__ = ('CONFIG', 'Config', 'utils', 'log')

ETC_DIR = '/etc/pytheon'
EGGS_DIR = '/var/share/pytheon/eggs'

if not os.path.isdir(EGGS_DIR):
    if 'PYTHEON_EGGS_DIR' in os.environ:
        EGGS_DIR = os.environ['PYTHEON_EGGS_DIR']
    else:
        cfg = Config.from_file(os.path.expanduser(join('~', '.buildout', 'default.cfg')))
        EGGS_DIR = cfg.buildout['eggs-directory'] or None

if not EGGS_DIR or not os.path.isdir(EGGS_DIR):
    raise OSError("Can't find pytheon eggs directory")

defaults = dict([('default_%s' % k[8:].lower(), v) for k, v in os.environ.items() if k.startswith('PYTHEON_')])
defaults['here'] = ETC_DIR
defaults['default_eggs_dir'] = EGGS_DIR
os.environ['PYTHON_EGGS'] = EGGS_DIR

if not os.path.isdir(ETC_DIR):
    CONFIG = Config(defaults=defaults)
    CONFIG.pytheon = dict(eggs_dir=EGGS_DIR)
else:
    CONFIG = Config.from_file(join(ETC_DIR, 'pytheon.ini'), **defaults)

utils.CONFIG = CONFIG

