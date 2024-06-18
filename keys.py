from libqtile.config import Key
from libqtile.config import Drag
from libqtile.config import Click
from libqtile.lazy import lazy
from my_qtile_functions import change_keymap, restart_qtile
from variables import HOME, WALLPAPER, terminal
from variables import mod, shft, alt, ctrl, spc


def group_types(groups, kind):
    group_keys = []
    if groups:
        if kind == "icons":
            for i, group in enumerate(groups):
                n_group = str(i)
                group_keys.extend([
                    Key([mod], n_group, lazy.group[group.name].toscreen(),
                        desc="Switch to group {}".format(group.name)),

                    Key([mod, "shift"], n_group, lazy.window.togroup(
                        group.name, switch_group=True),
                        desc="Switch to & move focused window to group {}"
                        .format(group.name)),
                ])
        elif kind == "numbers":
            for group in groups:
                group_keys.extend([
                    Key([mod], group.name, lazy.group[group.name].toscreen(),
                        desc="Switch to group {}".format(group.name)),

                    Key([mod, "shift"], group.name,
                        lazy.window.togroup(group.name, switch_group=True),
                        desc="Switch to & move focused window to group {}"
                        .format(group.name))
                ])
        return group_keys


def init_keys():
    keys = [
            # Switch between windows
            Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
            Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
            Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
            Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
            Key([mod], spc, lazy.layout.next(),
                desc="Move window focus to other window"),

            # Move programs between windows
            Key([mod, shft], "h", lazy.layout.shuffle_left(),
                desc="Move window to the left"),
            Key([mod, shft], "l", lazy.layout.shuffle_right(),
                desc="Move window to the right"),
            Key([mod, shft], "j", lazy.layout.shuffle_down(),
                desc="Move window down"),
            Key([mod, shft], "k", lazy.layout.shuffle_up(),
                desc="Move window up"),

            # Grow windows
            Key([mod, ctrl], "h", lazy.layout.grow_left(),
                desc="Grow window to the left"),
            Key([mod, "control"], "l", lazy.layout.grow_right(),
                desc="Grow window to the right"),
            Key([mod, ctrl], "j", lazy.layout.grow_down(),
                desc="Grow window down"),
            Key([mod, ctrl], "k", lazy.layout.grow_up(),
                desc="Grow window up"),
            Key([mod], "n", lazy.layout.normalize(),
                desc="Reset all window sizes"),

            # Toggle between split and unsplit sides of stack.
            # Split = all windows displayed
            # Unsplit = 1 window displayed, like Max layout, but still with
            # multiple stack panes
            Key([mod, shft], "Return", lazy.layout.toggle_split(),
                desc="Toggle between split and unsplit sides of stack"),
            Key([mod], "Return", lazy.spawn(terminal),
                desc="Launch terminal"),

            # Toggle between different layouts as defined below
            Key([mod], "Tab", lazy.next_layout(),
                desc="Toggle between layouts"),
            Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

            Key([mod, ctrl], "r", restart_qtile(),
                desc="Reload the config"),
            Key([mod, ctrl], "q", lazy.shutdown(), desc="Shutdown Qtile"),
            Key([mod], "r", lazy.spawncmd(),
                desc="Spawn a command using a prompt widget"),

            # My key bindings
            # >>> Spawn programs
            Key([mod], "m", lazy.spawn("rofi -show drun"),
                desc="Open Rofi Menu"),
            Key([mod], "f", lazy.spawn("firefox"), desc="Open Firefox"),
            Key([mod], "s", lazy.spawn("spotify"), desc="Open Spotify"),
            Key([ctrl, alt], "l",
                lazy.spawn("i3lock -i" + HOME + "Pictures/Wallpapers/" +
                WALLPAPER),
                desc="Lockscreen enable"),
            Key([ctrl, alt], "o", lazy.spawn("oblogout"),
                desc="Lockscreen enable"),
            Key([mod], "e", lazy.spawn("thunar"), desc="Open Files Manager"),
            Key([mod], "p", lazy.spawn("flameshot gui"),
                desc="Take a screenshot"),
            Key([mod, ctrl], "space", change_keymap(),
                desc="Change Key layout"),

            # >>> Set Volumen
            Key(
                [], "XF86AudioRaiseVolume",
                # lazy.spawn("amixer -q sset 'Master' 5%+")
                lazy.spawn("changevolume up"),
                desc="Increase sound"
            ),
            Key(
                [], "XF86AudioLowerVolume",
                # lazy.spawn("amixer -q sset 'Master' 5%-")
                lazy.spawn("changevolume down"),
                desc="Decrease sound"
            ),
            Key(
                [], "XF86AudioMute",
                # lazy.spawn("amixer -q sset 'Master' toggle")
                lazy.spawn("changevolume mute"),
                desc="Mute sound"
            ),

            # >>> Set Brightness
            Key(
                [], "XF86MonBrightnessUp",
                lazy.spawn("brightnessctl -s set +5%"),
                desc="Increase brightness"
            ),
            Key(
                [], "XF86MonBrightnessDown",
                lazy.spawn("brightnessctl -s set 5%-"),
                desc="Decrease brightness"
            ),

            # Set keybinding to navigate much better
            Key([mod], "Left", lazy.screen.prev_group()),
            Key([mod], "Right", lazy.screen.next_group()),
            Key(["control", "mod1"], "Tab", lazy.screen.prev_group()),
            Key(["mod1"], "Tab", lazy.screen.next_group()),
    ]
    return keys


def init_const_mouse():
    return [
        Drag([mod], "Button1", lazy.window.set_position_floating(),
            start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(),
            start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front())
    ]
