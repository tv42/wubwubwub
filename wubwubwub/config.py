"""WubWubWub configuration defaults."""
from twisted.web import static
from wubwubwub import vhost

# Set user/group to run under
# Usually, it runs under the www-data user and group.
username = 'www-data'
groupname = 'www-data'

# The root of the HTTP hierarchy
default = static.File('/var/www')

# Make sure it is easy to add new virtual hosts:
root = vhost.NameVirtualHost()
root.default = default

# This is the *Apache compatible* log file, not the twisted-style logfile.
# Leaving this as None will have no Apache compatible log file. Apache
# compatible logfiles are useful because there are quite a few programs
# which analyse them and display statistics. 
#logPath = None
logPath = '/var/log/wubwubwub/access.log'

# Generate the Site factory. You will not normally
# want to modify this line.
site = vhost.VhostLoggingNevowSite(root, logPath=logPath)
