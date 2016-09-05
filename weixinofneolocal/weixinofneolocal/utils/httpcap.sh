#!/bin/bash

tcpdump -i wlan0 tcp port 80 -w http.cap -vv -A &
