#!/bin/sh

PATH=/sbin:/bin:/usr/sbin:/usr/bin

[ -r /etc/default/twisted-web-users ] && . /etc/default/twisted-web-users

test -x /usr/bin/twistd2.2 || exit 0
test -r /usr/share/twisted-web/package-installed || exit 0

users=`getent passwd|awk -F: '$3>=1000 && $1!="nobody" {printf "grep -q %s /etc/shells && echo %s\n",$7,$1}'|sh`

case "$1" in
    start)
        echo -n "Starting twisted-web-users: "
        for user in $users;
            do home=`getent passwd $user|awk -F: '{print $6}'`
            command=$home/.twistd-command
            (cd $home && su - $user $command --pidfile=$home/.twistd.pid)
            echo -n "$user "
        done
        echo "Done."	
    ;;

    stop)
        echo -n "Stopping twisted-web-users: "
        for user in $users;
            do home=`getent passwd $user|awk -F: '{print $6}'`
            command=$home/.twistd-command
            kill `cat $home/twistd.pid`
            echo -n "$user "
        done
        echo "Done."	
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
