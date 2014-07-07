# -*- coding: utf-8 -*-

import os

# APP_ROOT = os.path.dirname(os.path.abspath(__file__))


# app.debug
DEBUG = True


# 'merge' or False
ASSETS_DEBUG = 'merge'
ASSETS_DIRECTORY = os.path.expanduser('~/tmp/assets_gen')


# strip spaces in html
HTML_COMPRESS = False


# Both 'static' and 'assets' endpoints will use CDN_URL_PREFIX.
# Protocol-less URLs also works. for eg. CDN_URL_PREFIX = '//127.0.0.1:5000'.
# Leave it empty string if you want to use relative URL
CDN_URL_PREFIX = ''
