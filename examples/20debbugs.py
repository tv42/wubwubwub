from twisted.web import static, twcgi

bugs = static.File('/var/lib/debbugs/www')
bugs.putChild('cgi-bin', twcgi.CGIDirectory('/var/lib/debbugs/www/cgi'))

# make it a child
default.putChild('bugs', bugs)
# or if it is a vhost
# root.addHost('bugs.example.com', bugs)
