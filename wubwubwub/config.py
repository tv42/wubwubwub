"""WubWubWub configuration defaults."""
from twisted.web import static

# Set user/group to run under
# Usually, it runs under the www-data user and group.
username = 'www-data'
groupname = 'www-data'

# The root of the HTTP hierarchy
default = static.File('/var/www')

# Make sure it is easy to add new virtual hosts:
root = vhost.NameVirtualHost()
root.default = default
