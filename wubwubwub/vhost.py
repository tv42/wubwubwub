from twisted.protocols import http
from nevow import appserver

class VhostLoggingNevowSite(appserver.NevowSite):
    def log(self, request):
        """
        Log a request's result to the logfile.
        Use combined log format prefixed with virtual host name.
        """
        if hasattr(self, "logFile"):
            line = '%r %s - - %s "%s" %d %s "%s" "%s"\n' % (
                request.getHeader('host'),
                request.getClientIP(),
                # request.getUser() or "-", # the remote user is almost never important
                http._logDateTime,
                '%s %s %s' % (request.method, request.uri, request.clientproto),
                request.code,
                request.sentLength or "-",
                request.getHeader("referer") or "-",
                request.getHeader("user-agent") or "-")
            self.logFile.write(line)
