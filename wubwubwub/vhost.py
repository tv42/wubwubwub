from twisted.protocols import http
from nevow import appserver

class VhostLoggingNevowSite(appserver.NevowSite):
    format = ('%(host)r %(ip)s - - %(datetime)s "%(req)s" '
              +'%(code)d %(sent)s "%(referer)s" "%(useragent)s"\n')
    def log(self, request):
        """
        Log a request's result to the logfile.
        Use combined log format prefixed with virtual host name.
        """
        logFile = getattr(self, 'logFile', None)
        if logFile is None:
            return
        data = {
            'host': request.getHeader('host'),
            'ip': request.getClientIP(),
            #'user': request.getUser() or "-", # the remote user is almost never important
            'datetime': http._logDateTime,
            'req': '%s %s %s' % (request.method, request.uri, request.clientproto),
            'code': request.code,
            'sent': request.sentLength or "-",
            'referer': request.getHeader("referer") or "-",
            'header': request.getHeader("user-agent") or "-",
            }
        self.logFile.write(format % data)
