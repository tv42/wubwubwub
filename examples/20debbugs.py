from twisted.web import static, twcgi
from wubwubwub import config

bugs = static.File('/var/lib/debbugs/www')
bugs.putChild('cgi-bin', twcgi.CGIDirectory('/var/lib/debbugs/www/cgi'))

# make it a child
config.default.putChild('bugs', bugs)
# or if it is a vhost
# config.root.addHost('bugs.example.com', bugs)
