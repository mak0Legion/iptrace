#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Piyush Singh(mak0Legion)'
SITENAME = 'Geo-Locate Internet Protocol (IP) Traffic'
SITEURL = ''
THEME = 'output5/theme'

PATH = 'content'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
STATIC_PATHS=['images']

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('PyGeoIP','http://code.google.com/p/pygeoip/'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/noobloops'),
			('Instagram', 'https://www.instagram.com/noob_loops'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#register cacause plugin
PLUGIN_PATHS = ['output4/theme/cacause']

#configure cacause
CACAUSE_DIR = "comments"
CACAUSE_GRAVATAR = True 
