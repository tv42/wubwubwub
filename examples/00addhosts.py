# Add all hosts in a given directory as virtual hosts.
# In order to use this, change '/var/www/vhost' to the directory
# in which you keep the files for the virtual hosts and copy this file to
# /etc/twisted-web/local.d
#
from twisted.web import static
import os

vhostDir = '/var/www/vhost/'

for file in os.listdir(vhostDir):
    root.addHost(file, static.File(os.path.join(vhostDir, file)))
