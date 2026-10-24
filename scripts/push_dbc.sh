#!/usr/bin/bash

USER="pi"
HOST="192.168.73.1"

scp *.dbc "$USER@$HOST:/home/pi/Formula-DBC/"
ssh "$USER@$HOST" "/home/pi/datalogger/update.sh"
