# Add .rpy support to the default web site.
# 
# To use this file, cp 01processrpy.py /etc/wubwubwub/local.d
#
from twisted.web import script
from wubwubwub import config

config.default.processors['.rpy'] = script.ResourceScript

# To make .rpy processing transparent:
# config.default.ignoreExt('rpy')
