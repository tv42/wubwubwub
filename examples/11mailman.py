# Make sure mailman links work
from twisted.web import twcgi
default.putChild('mailman', twcgi.CGIDirectory('/usr/lib/cgi-bin'))
