from twisted.web import static, server
from twisted.application import internet
from wubwubwub import config

directory = '/var/www/vhost/' 

# Change this if you want to use other processors or indexNames
processors = config.default.processors
indexNames = config.default.indexNames

resource = static.File(directory)
site = server.Site(resource,
                   # Uncomment if you want logging
                   ## logPath='/var/log/wubwubwub/ncsa.81',
                   )
service = internet.TCPServer(81, site)
service.setServiceParent(config.application)
