from twisted.web import static, server

directory = '/var/www/vhost/' 

# Change this if you want to use other processors or indexNames
processors = default.processors
indexNames = default.indexNames

resource = static.File(os.path.join(directory))
site = server.Site(resource,
# Uncomment if you want logging
#logPath='/var/log/wubwubwub/ncsa.81'
)
application.listenTCP(81, site)
