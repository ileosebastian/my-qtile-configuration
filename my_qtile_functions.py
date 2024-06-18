from libqtile.lazy import lazy
from libqtile import hook
from libqtile import widget
import subprocess

from variables import HOME


def get_separator():
    return widget.Sep(
                    linewidth=2,
                    padding=2,
                    size_percent=100
                )

@lazy.function
def set_key_map(qtile):
    qtile.cmd_spawn("setxkbmap us")


@lazy.function
def restart_qtile(qtile):
    qtile.cmd_reload_config()
    # qtile.cmd_restart()


@lazy.function
def change_keymap(qtile):
    qtile.cmd_spawn("changekeymap")

    textbox = qtile.widgets_map["textbox"]
    txt_parsed = textbox.info()["text"].split(' ')
    if "ENG" in txt_parsed:
        qtile.widgets_map["textbox"].update("ESP")
    elif "ESP" in txt_parsed:
        qtile.widgets_map["textbox"].update("ENG")


@hook.subscribe.startup_once
def autostart():
    subprocess.Popen([HOME + '.config/qtile/autostart.sh'])


