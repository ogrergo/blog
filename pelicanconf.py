#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Louis van Beurden'
SITENAME = u'Louis van Beurden'
SITEURL = ''

PATH = 'content'

THEME='attila'
STATIC_PATHS = ['img', 'static']
FAVICON = 'img/favicon.ico'
CUSTOM_CSS = 'static/custom.css'


HEADER_COLOR = 'black'



TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('IEML Dictionary', 'https://dictionary.ieml.io'),
		 ('Intlekt', 'https://intlekt.io'))

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/LouisvanBeurden'),
		   ('github', 'https://github.com/ogrergo'),
          ('linkedin', 'https://www.linkedin.com/in/louis-van-beurden-a94844b0/'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
