# Add all hosts in a given directory as virtual hosts.
# In order to use this, change '/var/www/vhost' to the directory
# in which you keep the files for the virtual hosts and copy this file to
# /etc/wubwubwub/local.d
#
from twisted.web import static
import os
from wubwubwub import config

# Directory where the virtual hosts are kept
vhostDir = '/var/www/vhost/'
# Whether to add www.<vhost> as alias for <vhost>
addWWW = 0

# Change this if you want to use other processors or indexNames
processors = config.default.processors
indexNames = config.default.indexNames

for filename in os.listdir(vhostDir):
    resource = static.File(os.path.join(vhostDir, filename))
    resource.processors = processors
    resource.indexNames = indexNames
    config.root.addHost(filename, resource)
    if addWWW:
        root.addHost('www.'+filename, resource)
