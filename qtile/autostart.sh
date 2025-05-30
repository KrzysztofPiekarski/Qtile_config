#!/bin/sh

xrandr --output Virtual-1 --mode 1920x1080
setxkbmap pl &

# Ustaw tapetę
# feh --bg-scale ~/Obrazy/wallpaper.jpg &
nitrogen --restore &

# Compositor dla przezroczystości i efektów
picom --config ~/.config/picom/picom.conf &

# Network Manager applet
nm-applet &

# Bluetooth applet
blueman-applet &

# Kontrola jasności (dla laptopów)
xfce4-power-manager &

# Autostart aplikacji
# Discord
# discord &

# Spotify
# spotify &

# Redshift (filtr niebieskiego światła)
redshift-gtk &

# Clipboard manager
clipit &

# Automatyczne montowanie dysków
udiskie -t &