#!/bin/sh

# Key Configuration
setxkbmap us

# Screen Configuration
brightnessctl -s set 180

# System Icons
# udiskie -t &
nm-applet &
# volumeicon &
# cbatticon -u 5 &
# set wallpaper
nitrogen --restore &

flameshot &
picom &
