#!/bin/sh

PATH=/sbin:/bin:/usr/sbin:/usr/bin

[ -r /etc/default/twisted-web-users ] && . /etc/default/twisted-web-users

test -x /usr/bin/twistd2.2 || exit 0
test -r /usr/share/twisted-web/package-installed || exit 0

if [ -r /etc/twisted-web/twisted-web-users.allow ]; then
    users=`cat /etc/twisted-web/twisted-web-users.allow`
else
    users=`getent passwd|awk -F: '$3>=1000 && $1!="nobody" {printf "grep -q %s /etc/shells && echo %s\n",$7,$1}'|sh`
    if [ -r /etc/twisted-web/twisted-web-users.deny ]; then
        temp_users=`for user in $users;do echo $user;done | sort | comm -2 -3 - <(sort /etc/twisted-web-users.deny)`
        users=$temp_users
    fi
fi

case "$1" in
    start)
        echo -n "Starting twisted-web-users: "
        for user in $users;
            do home=`getent passwd $user|awk -F: '{print $6}'`
            command=$home/.twisted-command
            [ -e $command ] && (cd $home && su - $user -- $command --pidfile=$home/.twistd.pid)
            echo -n "$user "
        done
        echo "Done."	
    ;;

    stop)
        echo -n "Stopping twisted-web-users: "
        for user in $users;
            do home=`getent passwd $user|awk -F: '{print $6}'`
            command=$home/.twisted-command
            [ -e $home/.twistd.pid ] && kill `cat $home/.twistd.pid`
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
