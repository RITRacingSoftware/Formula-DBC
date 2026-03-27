#!/usr/bin/bash

USER="pi"
HOST="datalogger.local"

scp *.dbc "$USER@$HOST:/home/pi/Formula-DBC/"
ssh "$USER@$HOST" "/home/pi/datalogger/update.sh"
