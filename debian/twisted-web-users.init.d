#!/bin/sh
PATH=/sbin:/bin:/usr/sbin:/usr/bin

pidfile=/var/run/twisted-web-users.pid
rundir=/var/lib/twisted-web/
file=/etc/twisted-web/twisted-web-users
logfile=/var/log/twisted-web/twisted-web-users.log
more_args=--no_save

[ -r /etc/default/twisted-web-users ] && . /etc/default/twisted-web-users

test -x /usr/bin/twistd2.3 || exit 0
test -r $file || exit 0
test -r /usr/share/twisted-web/package-installed || exit 0


case "$1" in
    start)
        echo -n "Starting twisted-web-users: process-manager"
        start-stop-daemon --start --quiet --exec /usr/bin/twistd2.3 --  \
                          --pidfile=$pidfile --rundir=$rundir --python=$file\
                          --logfile=$logfile --quiet $more_args
        echo "."	
    ;;

    stop)
        echo -n "Stopping twisted-web-users: process-manager"
        start-stop-daemon --stop --quiet --pidfile $pidfile
        echo "."	
    ;;

    restart)
        $0 stop
        $0 start
    ;;

    force-reload)
        $0 restart
    ;;

    *)
        echo "Usage: /etc/init.d/twisted-web-users {start|stop|restart|force-reload}" >&2
        exit 1
    ;;
esac

exit 0
