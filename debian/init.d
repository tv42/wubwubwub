#!/bin/sh

PATH=/sbin:/bin:/usr/sbin:/usr/bin

pidfile=/var/run/wubwubwub.pid
rundir=/var/lib/wubwubwub/
file=/etc/wubwubwub/wubwubwub
more_args=--no_save

[ -r /etc/default/wubwubwub ] && . /etc/default/wubwubwub

test -x /usr/bin/twistd2.3 || exit 0
test -r $file || exit 0
test -r /usr/share/wubwubwub/package-installed || exit 0
test -r /etc/wubwubwub/disable && . /etc/wubwubwub/disable


case "$1" in
    start)
        echo -n "Starting wubwubwub: twistd"
        start-stop-daemon --start --quiet --exec /usr/bin/twistd2.3 --  \
                          --pidfile=$pidfile --rundir=$rundir --python=$file\
                          --syslog --prefix=wubwubwub $more_args
        echo "."	
    ;;

    stop)
        echo -n "Stopping wubwubwub: twistd"
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
        echo "Usage: /etc/init.d/wubwubwub {start|stop|restart|force-reload}" >&2
        exit 1
    ;;
esac

exit 0
