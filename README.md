# 🎛️ Qtile Configuration

A clean, functional, and modern Qtile setup with gradient-themed colors and intuitive keybindings. Designed for speed, aesthetics, and productivity.

## 🖥️ Preview

This configuration includes:
- A modern powerline-style bar
- Minimal and responsive layout
- Integration with rofi, playerctl, flameshot, brightnessctl, pactl
- Multimedia key support
- Nerd Font-powered icons

## 📦 Required Packages

To run this Qtile config properly, ensure you have the following installed:

### 🔧 Core

sudo pacman -S qtile xorg-xinit xorg-xrandr

### 🛠️ Utilities

sudo pacman -S rofi flameshot brightnessctl playerctl pulseaudio alsa-utils xfce4-power-manager bluez bluez-utils blueman nitrogen networkmanager network-manager-applet 
yay -S clipit

### 🎨 Fonts 

Install Nerd Fonts (e.g., FiraCode, JetBrainsMono):
sudo pacman -S ttf-meslo-nerd ttf-hack-nerd powerline-fonts ttf-font-awesome ttf-jetbrains-mono noto-fonts-emoji 

Alternatively, download from: https://www.nerdfonts.com/

### 📂 Installation

Place config.py and additional files in:
~/.config/qtile/
Add to your ~/.xinitrc:
exec qtile
Launch with:
startx

### ⌨️ Keybindings

| Keys                    | Action                                  |
| ----------------------- | --------------------------------------- |
| `Mod + h/j/k/l`         | Move between windows                    |
| `Mod + Shift + h/j/k/l` | Move windows                            |
| `Mod + Ctrl + h/j/k/l`  | Resize windows                          |
| `Mod + Return`          | Launch terminal                         |
| `Mod + d`               | Launch app menu (`rofi -show drun`)     |
| `Mod + r`               | Run command prompt                      |
| `Mod + m`               | Toggle music playback (via `playerctl`) |
| `Mod + Shift + c`       | Close focused window                    |
| `Mod + Ctrl + r/q`      | Reload/Quit Qtile                       |
| `Mod + 1-9`             | Switch workspace                        |
| `Mod + Shift + 1-9`     | Move window to workspace                |
| `Print`                 | Take screenshot (`flameshot gui`)       |
| `XF86Audio*`            | Audio control                           |
| `XF86MonBrightness*`    | Brightness control                      |


### 🎨 Color Theme

- A gentle, modern color palette based on pastel and cool tones:
- Background: #1a1b26, #24283b
- Foreground: #a9b1d6, #565f89
- Accents: Blue, Purple, Cyan, Green, Orange, Red
- Bar Style: Powerline segments with TextBox separators

### 🧩 Bar Widgets

Widgets include:
- App launcher icon
- Workspace groups
- Window name
- System tray
- CPU & memory usage
- Audio volume (PulseAudio or ALSA)
- Brightness slider

### 🚀 Tips & Notes

- Add autostart programs using @hook.subscribe.startup_once
- You can autostart: picom (compositor), feh (wallpapers), dunst (notifications), etc.
- Use alsamixer or pavucontrol depending on your audio backend (ALSA or PulseAudio)

### 🛠️ Audio Notes

You can switch between two widgets:
- For PulseAudio (PipeWire, default in many distros):
widget.PulseVolume(...)
- For ALSA (if no PulseAudio is running):
widget.Volume(...)

Make sure to install the appropriate utilities (alsa-utils, pulseaudio, etc.).

### 💬 Support

Made with passion for minimalism and performance.
If you need help, feel free to reach out or open an issue.
Enjoy your Qtile experience!

