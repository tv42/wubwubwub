# Add .rpy support to the default web site.
# 
# To use this file, cp 01processrpy.py /etc/twisted-web/local.d
#
from twisted.web import script, static

if isinstance(root.default, static.File):
    root.processors['.rpy'] = script.ResourceScript
