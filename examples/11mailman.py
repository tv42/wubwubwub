# Make sure mailman links work
from twisted.web import twcgi, static
default.putChild('mailman', twcgi.CGIDirectory('/usr/lib/cgi-bin'))

# Comment this out if you do not want to use the pipermail archiver
default.putChild('pipermail', static.File('/var/lib/mailman/archives/public'))
