# If this server serves from behind a reverse proxy, then it
# may have the wrong idea about its hostname/port. Since this
# information belongs in the reverse proxy configuration, it should
# be transmitted in the URL.
# After copyring this file to /etc/twisted-web/local.d/, configure
# the reverse proxy to translate:
# http://example.com/foo/bar/baz.html to
# http://internal-host/vhost/http/example.com/foo/bar/baz.html
#
from twisted.web import vhost

root.default.putChild('vhost', vhost.VHostMonsterResource())
