from twisted.web import twcgi
from wubwubwub import config

# enable /var/www/cgi-lib as a place for CGI modules.
# Note that this means that write access to /var/www/cgi-lib grants
# the ability to execute code as www-data
config.default.putChild('cgi-lib', twcgi.CGIDirectory('/var/www/cgi-lib'))
