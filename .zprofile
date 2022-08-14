export MOZ_ENABLE_WAYLAND=1
export TERM=alacritty
export EDITOR=nvim

if [ -z "${DISPLAY}" ] && [ "$(tty)" = "/dev/tty1"  ] ; then
    exec sway
fi
