#!/usr/bin/env bash
PORT=${PORT:-5000}
MAX_DISPLAY_LEN=${MAX_DISPLAY_LEN:-5000}


tmux new-session \; \
  send-keys "python /dumbwebhook/dumbwebhook/dumbwebhook.py --port $PORT --max-len-to-display $MAX_DISPLAY_LEN" C-m \; \
  split-window -v \; \
  send-keys "/dumbwebhook/bin/ngrok http -inspect=0 $PORT" C-m \;