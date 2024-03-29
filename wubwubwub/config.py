"""WubWubWub configuration defaults."""
from twisted.application import service
from nevow import static, vhost
from wubwubwub.vhost import VhostLoggingNevowSite

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

# Write separate access log files for each virtual host in this
# directory. Requests with no Host: header still get written to
# logPath. Set to None to make all requests go to logPath.
#logDir = None
logDir = '/var/log/wubwubwub/vhost'

# Generate the Site factory. You will not normally
# want to modify this line.
site = VhostLoggingNevowSite(root, logPath=logPath, logDir=logDir)

# Generate the Application.
application = service.Application("wubwubwub")
