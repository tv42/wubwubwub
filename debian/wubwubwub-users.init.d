#!/bin/sh
PATH=/sbin:/bin:/usr/sbin:/usr/bin

pidfile=/var/run/wubwubwub-users.pid
rundir=/var/lib/wubwubwub/
file=/etc/wubwubwub/wubwubwub-users
more_args=--no_save

[ -r /etc/default/wubwubwub-users ] && . /etc/default/wubwubwub-users

test -x /usr/bin/twistd2.3 || exit 0
test -r $file || exit 0
test -r /usr/share/wubwubwub/package-installed || exit 0


case "$1" in
    start)
        echo -n "Starting wubwubwub-users: process-manager"
        start-stop-daemon --start --quiet --exec /usr/bin/twistd2.3 --  \
                          --pidfile=$pidfile --rundir=$rundir --python=$file\
                          --syslog --prefix=wubwubwub-users --quiet $more_args
        echo "."	
    ;;

    stop)
        echo -n "Stopping wubwubwub-users: process-manager"
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
        echo "Usage: /etc/init.d/wubwubwub-users {start|stop|restart|force-reload}" >&2
        exit 1
    ;;
esac

exit 0
