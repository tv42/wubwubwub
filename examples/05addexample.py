# In order to add a custom virtual host, copy this file into
# /etc/wubwubwub/local.d/05add<host name>.py, change
# "example.com" and "/var/www/example" to the hostname and
# directory you want, and change the various settings as per
# the comments.
#
from twisted.web import script, static, twcgi

vhostName, vhostRoot= "example.com", "/var/www/example"
resource = static.File('/var/www/'+vhostRoot)
root.addHost(vhostName, vhostResource)

# The default processors in Twisted, by file extension.
# These make some file extensions not being sent to the user,
# but rather evaluated in various ways.
#
# Do *NOT* turn any of this on if untrusted users can put files
# in the document hierarchy.
resource.processors = {
#    '.cgi': twcgi.CGIScript,
#    '.php3': twcgi.PHP3Script,
#    '.php': twcgi.PHPScript,
#    '.epy': script.PythonScript,
#    '.rpy': script.ResourceScript,
#    '.trp': trp.ResourceUnpickler,
}

# Change this if you want default mime-type to be different:
# resource.defaultType = 'text/html'

# Add more mime-types
resource.contentTypes = root.contentTypes.copy()
# resource.contentTypes['extension'] = 'mime/type'

# Uncomment this so /path/to/foo can serve /path/to/foo.bar
# resource.ignoreExt('*')
# Or ignore specific extensions
# resource.ignoreExt('html')
# resource.ignoreExt('rpy')

# Add more indexes
# http://host/foo/ will serve index.html, index.rpy or index.php,
# the first which exists.
# If none exist, it will generate a directory listing.
#
resource.indexNames = [
    'index.html',
#     'index.rpy',
#     'index.php',
]
