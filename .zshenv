# . "$HOME/.cargo/env"

export EDITOR=nvim
export TERM=alacritty

if [ "$XDG_SESSION_TYPE" = "wayland" ]; then
    export MOZ_ENABLE_WAYLAND=1
else 
    export MOZ_ENABLE_WAYLAND=0
fi
source $HOME/.cargo/env
