# -*- coding: utf-8 -*-
"""Create an application instance."""
from flask.helpers import get_debug_flag

from hackvt2016.app import create_app
from hackvt2016.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)
