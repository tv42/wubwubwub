#!/bin/sh

PATH=/sbin:/bin:/usr/sbin:/usr/bin

pidfile=/var/run/twisted-web.pid
rundir=/var/lib/twisted-web/
file=/etc/twisted-web/twisted-web
more_args=--no_save

[ -r /etc/default/twisted-web ] && . /etc/default/twisted-web

test -x /usr/bin/twistd2.3 || exit 0
test -r $file || exit 0
test -r /usr/share/twisted-web/package-installed || exit 0
test -r /etc/twisted-web/disable && . /etc/twisted-web/disable


case "$1" in
    start)
        echo -n "Starting twisted-web: twistd"
        start-stop-daemon --start --quiet --exec /usr/bin/twistd2.3 --  \
                          --pidfile=$pidfile --rundir=$rundir --python=$file\
                          --syslog --prefix=twisted-web $more_args
        echo "."	
    ;;

    stop)
        echo -n "Stopping twisted-web: twistd"
        start-stop-daemon --stop --quiet --pidfile $pidfile
        while [ -f $pidfile ] && /bin/kill -0 `cat $pidfile`; do \
                 echo -n "."; \
        done
        echo " done."	
    ;;

    restart)
        $0 stop
        $0 start
    ;;

    force-reload)
        $0 restart
    ;;

    *)
        echo "Usage: /etc/init.d/twisted-web {start|stop|restart|force-reload}" >&2
        exit 1
    ;;
esac

exit 0
