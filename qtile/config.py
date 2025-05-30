#     ██████     █████     ███  ████          
#   ███░░░░███  ░░███     ░░░  ░░███          
#  ███    ░░███ ███████   ████  ░███   ██████ 
# ░███     ░███░░░███░   ░░███  ░███  ███░░███
# ░███   ██░███  ░███     ░███  ░███ ░███████ 
# ░░███ ░░████   ░███ ███ ░███  ░███ ░███░░░  
#  ░░░██████░██  ░░█████  █████ █████░░██████ 
#    ░░░░░░ ░░    ░░░░░  ░░░░░ ░░░░░  ░░░░░░  
# ~/.config/qtile/config.py

import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# Ustawienia globalne
mod = "mod4"  # Windows key
terminal = guess_terminal()

# Paleta kolorów - Nowoczesny gradient
colors = {
    'bg_primary': '#1a1b26',      # Ciemny background
    'bg_secondary': '#24283b',    # Jasniejszy background
    'fg_primary': '#a9b1d6',     # Główny kolor tekstu
    'fg_secondary': '#565f89',    # Drugorzędny kolor tekstu
    'accent_blue': '#7aa2f7',     # Niebieski akcent
    'accent_purple': '#bb9af7',   # Fioletowy akcent
    'accent_cyan': '#7dcfff',     # Cyjan akcent
    'accent_green': '#9ece6a',    # Zielony akcent
    'accent_orange': '#ff9e64',   # Pomarańczowy akcent
    'accent_red': '#f7768e',      # Czerwony akcent
    'warning': '#e0af68',         # Żółty warning
    'transparent': '#00000000',   # Przezroczysty
}

# Keybindings
keys = [
    # Przełączanie między oknami
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    
    # Przenoszenie okien
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    
    # Zmiana rozmiaru okien
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),
    
    # Przełączanie layoutów
    Key([mod], "Tab", lazy.next_layout()),
    
    # Zamykanie okien
    Key([mod, "shift"], "c", lazy.window.kill()),
    
    # Restart/Quit Qtile
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),
    
    # Aplikacje
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], "d", lazy.spawn("rofi -show drun")),
    Key([], "Print", lazy.spawn("flameshot gui")),
    Key([mod], "m", lazy.spawn("playerctl play-pause")),
    
    # Kontrola głośności
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    
    # Kontrola jasności
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

# Grupy (workspace)
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
    ])

# Layouty
layouts = [
    layout.Columns(
        border_focus=colors['accent_blue'],
        border_normal=colors['bg_secondary'],
        border_width=2,
        margin=8,
        border_on_single=True,
    ),
    layout.Max(
        margin=8,
        border_focus=colors['accent_purple'],
        border_normal=colors['bg_secondary'],
        border_width=2,
    ),
    layout.Floating(
        border_focus=colors['accent_cyan'],
        border_normal=colors['bg_secondary'],
        border_width=2,
    ),
]

# Funkcje pomocnicze dla widżetów
def create_powerline(fg_color, bg_color, reverse=False):
    """Tworzy separator w stylu powerline"""
    if reverse:
        return widget.TextBox(
            text="",
            fontsize=16,
            foreground=fg_color,
            background=bg_color,
            padding=0,
        )
    else:
        return widget.TextBox(
            text="",
            fontsize=16,
            foreground=fg_color,
            background=bg_color,
            padding=0,
        )

# Konfiguracja ekranu
screens = [
    Screen(
        top=bar.Bar(
            [
                # Logo/Menu
                widget.TextBox(
                    text=" 󰣇 ",
                    fontsize=18,
                    foreground=colors['accent_blue'],
                    background=colors['bg_primary'],
                    mouse_callbacks={'Button1': lambda: lazy.spawn("rofi -show drun")()},
                    padding=10,
                ),
                
                # Separator
                create_powerline(colors['bg_secondary'], colors['bg_primary']),
                
                # Grupy
                widget.GroupBox(
                    active=colors['fg_primary'],
                    inactive=colors['fg_secondary'],
                    highlight_color=colors['accent_purple'],
                    highlight_method="line",
                    this_current_screen_border=colors['accent_blue'],
                    block_highlight_text_color=colors['fg_primary'],
                    background=colors['bg_secondary'],
                    borderwidth=3,
                    padding_x=8,
                    padding_y=6,
                    margin_x=0,
                    margin_y=3,
                    fontsize=12,
                    disable_drag=True,
                ),
                
                # Separator
                create_powerline(colors['bg_primary'], colors['bg_secondary']),
                
                # Aktywne okno
                widget.WindowName(
                    foreground=colors['fg_primary'],
                    background=colors['bg_primary'],
                    fontsize=11,
                    padding=10,
                    max_chars=50,
                ),
                
                # Spacer
                widget.Spacer(background=colors['bg_primary']),
                
                # System Tray
                widget.Systray(
                    background=colors['bg_primary'],
                    padding=5,
                    icon_size=18,
                ),
                
                widget.Sep(
                    linewidth=0,
                    padding=10,
                    background=colors['bg_primary'],
                ),
                
                # Separator CPU
                create_powerline(colors['accent_red'], colors['bg_primary'], reverse=True),
                
                # CPU
                widget.TextBox(
                    text=" 󰻠 ",
                    fontsize=16,
                    foreground=colors['bg_primary'],
                    background=colors['accent_red'],
                    padding=0,
                ),
                widget.CPU(
                    format='{load_percent}%',
                    foreground=colors['bg_primary'],
                    background=colors['accent_red'],
                    fontsize=11,
                    padding=5,
                    update_interval=2,
                ),
                
                # Separator RAM
                create_powerline(colors['accent_orange'], colors['accent_red'], reverse=True),
                
                # RAM
                widget.TextBox(
                    text=" 󰍛 ",
                    fontsize=16,
                    foreground=colors['bg_primary'],
                    background=colors['accent_orange'],
                    padding=0,
                ),
                widget.Memory(
                    format='{MemUsed: .0f}{mm}',
                    foreground=colors['bg_primary'],
                    background=colors['accent_orange'],
                    fontsize=11,
                    padding=5,
                    update_interval=5,
                ),
                
                # Separator Volume
                create_powerline(colors['accent_green'], colors['accent_orange'], reverse=True),
                
                # Volume
                widget.TextBox(
                    text=" 󰕾 ",
                    fontsize=16,
                    foreground=colors['bg_primary'],
                    background=colors['accent_green'],
                    padding=0,
                ),
                 #  widget.PulseVolume(
                 #     foreground=colors['bg_primary'],
                 #     background=colors['accent_green'],
                 #     fontsize=11,
                 #     padding=5,
                 #     limit_max_volume=True,
                 #     mouse_callbacks={
                 #         'Button3': lazy.spawn("pavucontrol")(),
                 #     },
		widget.Volume(
    		   foreground=colors['bg_primary'],
    		   background=colors['accent_green'],
    		   fontsize=11,
                   padding=5,
                   mouse_callbacks={
                       'Button3': lazy.spawn("alsamixer"),
                       'Button1': lazy.spawn("amixer set Master toggle"),
                       'Button4': lazy.spawn("amixer set Master 5%+"),
                       'Button5': lazy.spawn("amixer set Master 5%-"),
                   },
                ),
                
                # Separator Brightness (tylko dla laptopów)
                create_powerline(colors['accent_cyan'], colors['accent_green'], reverse=True),
                
                # Brightness
                widget.TextBox(
                    text=" 󰃞 ",
                    fontsize=16,
                    foreground=colors['bg_primary'],
                    background=colors['accent_cyan'],
                    padding=0,
                ),
                widget.Backlight(
                    backlight_name='nvidia_0',  # Zmień na odpowiedni dla twojego systemu
                    format='{percent:2.0%}',
                    foreground=colors['bg_primary'],
                    background=colors['accent_cyan'],
                    fontsize=11,
                    padding=5,
                    step=5,
	            mouse_callbacks={
                    	'Button4': lazy.spawn("brightnessctl set +5%"),
        	    	'Button5': lazy.spawn("brightnessctl set 5%-"),
        	    	'Button1': lazy.spawn("brightnessctl set 50%")
    		    }
                ),
                
                # Separator Battery (tylko dla laptopów)
                create_powerline(colors['accent_purple'], colors['accent_cyan'], reverse=True),
                
                # Battery
                widget.Battery(
                    format=' {char} {percent:2.0%}',
                    charge_char='󰂄',
                    discharge_char='󰁹',
                    empty_char='󰂎',
                    full_char='󰁹',
                    unknown_char='󰂑',
                    foreground=colors['bg_primary'],
                    background=colors['accent_purple'],
                    fontsize=11,
                    padding=5,
                    low_percentage=0.2,
                    low_foreground=colors['accent_red'],
                    show_short_text=False,
                ),
                
                # Separator Date
                create_powerline(colors['accent_blue'], colors['accent_purple'], reverse=True),
                
                # Calendar/Date
                widget.TextBox(
                    text=" 󰸗 ",
                    fontsize=16,
                    foreground=colors['bg_primary'],
                    background=colors['accent_blue'],
                    padding=0,
                ),
                widget.Clock(
                    format='%d/%m/%Y',
                    foreground=colors['bg_primary'],
                    background=colors['accent_blue'],
                    fontsize=11,
                    padding=5,
                    mouse_callbacks={
                        'Button1': lambda: lazy.spawn("gnome-calendar")(),
                    },
                ),
                
                # Separator Time
                create_powerline(colors['bg_secondary'], colors['accent_blue'], reverse=True),
                
                # Time
                widget.TextBox(
                    text=" 󰥔 ",
                    fontsize=16,
                    foreground=colors['fg_primary'],
                    background=colors['bg_secondary'],
                    padding=0,
                ),
                widget.Clock(
                    format='%H:%M',
                    foreground=colors['fg_primary'],
                    background=colors['bg_secondary'],
                    fontsize=12,
                    padding=10,
                ),
                
                # Power Menu
                widget.TextBox(
                    text=" ⏻ ",
                    fontsize=16,
                    foreground=colors['accent_red'],
                    background=colors['bg_secondary'],
                    mouse_callbacks={
                        'Button1': lambda: lazy.spawn("rofi -show power-menu -modi power-menu:~/.local/bin/rofi-power-menu")(),
                    },
                    padding=10,
                ),
            ],
            30,  # Wysokość bara
            background=colors['bg_primary'],
            opacity=0.95,
            margin=[8, 8, 0, 8],  # top, right, bottom, left
        ),
    ),
]

# Mouse callbacks
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# Pozostałe ustawienia
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="gnome-calculator"),
        Match(wm_class="file-roller"),
    ],
    border_focus=colors['accent_cyan'],
    border_normal=colors['bg_secondary'],
    border_width=2,
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None

# Startup applications
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

# Auto-restart na zmianę konfiguracji
wmname = "LG3D"
