if [ -z "${DISPLAY}" ] && [ "$(tty)" = "/dev/tty1"  ] ; then
    if [ "$HOST"="old-lenovo" ] || ["$HOST"="konstantinos-thinkpad" ]; then
        exec sway
    fi
    if [ "$HOST"="konstantinos-desktop" ]; then
        exec startx
    fi
fi
