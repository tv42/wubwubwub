import os, re
from twisted.internet import defer
from twisted.protocols import http
from nevow import appserver

class VhostLoggingNevowSite(appserver.NevowSite):
    format = ('%(ip)s - - %(datetime)s "%(req)s" '
              +'%(code)d %(sent)s "%(referer)s" "%(useragent)s"\n')

    def __init__(self, *args, **kwargs):
        self.logDir = kwargs.pop('logDir', None)
        appserver.NevowSite.__init__(self, *args, **kwargs)

    LEADINGDOTS = re.compile('\.+')
    def safeHostname(self, host):
        """
        Make a potentially hostile Host: header safe to use as a
        filename (on Unix).
        """
        s = host.replace('/', '_')
        match = self.LEADINGDOTS.match(s)
        if match is not None:
            s = '_'*match.end() + s[match.end():]
        return s

    def writeLog(self, logFile, request):
        """
        Actually write the log entry. May return a Deferred, though
        only cleanup actions will be delayed until its completion --
        most importantly, other writeLog calls may happen even before
        the Deferred triggers.
        """
        data = {
            'host': request.getHeader('host'),
            'ip': request.getClientIP(),
            #'user': request.getUser() or "-", # the remote user is almost never important
            'datetime': http._logDateTime,
            'req': '%s %s %s' % (request.method, request.uri, request.clientproto),
            'code': request.code,
            'sent': request.sentLength or "-",
            'referer': request.getHeader("referer") or "-",
            'useragent': request.getHeader("user-agent") or "-",
            }
        logFile.write(self.format % data)

    def log(self, request):
        """
        Log a HTTP request to the configured logfile in combined log
        format.
        """
        host = request.getHeader('host')
        logFile = getattr(self, 'logFile', None)
        cleanup = defer.Deferred()

        if self.logDir is not None and host is not None:
            logPath = os.path.join(self.logDir,
                                   '%s.log' % self.safeHostname(host))
            logFile = file(logPath, 'a', 0)
            cleanup.addBoth(lambda _: logFile.close())

        if logFile is None:
            d = defer.succeed(None)
        else:
            d = defer.maybeDeferred(self.writeLog, logFile, request)
        d.chainDeferred(cleanup)
