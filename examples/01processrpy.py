# Add .rpy support to the default web site.
# 
# To use this file, cp 01processrpy.py /etc/twisted-web/local.d
#
from twisted.web import script, static

default.processors['.rpy'] = script.ResourceScript

# To make .rpy processing transparent:
# default.ignoreExt('rpy')
