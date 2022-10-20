#/usr/bin/bash

# If an instance of wf-recorder is running under this user kill it with SIGINT and exit
pkill --euid "$USER" --signal SIGINT wf-recorder && exit

# Capture video using slup for screen area
# timeout and exit after 10 minutes as user has almost certainly forgotten it's running
timeout 600 wf-recorder -g "$(slurp)" --file=$HOME/media/Videos/recordings/$(date +"%F_%T").mp4 || exit
