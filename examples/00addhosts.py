# Add all hosts in a given directory as virtual hosts.
# In order to use this, change '/var/www/vhost' to the directory
# in which you keep the files for the virtual hosts and copy this file to
# /etc/twisted-web/local.d
#
from twisted.web import static
import os

# Directory where the virtual hosts are kept
vhostDir = '/var/www/vhost/'
# Whether to add www.<vhost> as alias for <vhost>
addWWW = 0

# Change this if you want to use other processors or indexNames
processors = default.processors
indexNames = default.indexNames

for file in os.listdir(vhostDir):
    resource = static.File(os.path.join(vhostDir, file))
    resource.processors = processors
    resource.indexNames = indexNames
    root.addHost(file, resource)
    if addWWW:
        root.addHost('www.'+file, resource)
