from libqtile import bar
from libqtile import widget
from libqtile.config import Screen
from libqtile.lazy import lazy
from my_qtile_functions import get_separator
from my_qtile_functions import change_keymap
import arcobattery

from variables import HOME, default_font, default_font_bold
from theming import theme as qtile_theme


theme = qtile_theme.theme


def init_screens():
    return [
        Screen(
            top=bar.Bar(
                [
                    widget.GroupBox(
                        urgent_alert_method='text',
                        disable_drag=True,
                        highlight_method='block',
                        borderwidth=1,
                        font=default_font,
                        fontsize=16,
                        padding=0,
                        padding_x=8, padding_y=2,
                        margin=10,
                        margin_x=0, margin_y=4
                    ),
                    widget.Prompt(fmt="  : {}", prompt=""),
                    widget.Spacer(),
                    get_separator(),
                    widget.CheckUpdates(
                        background=theme['Acolor0'],
                        fontsize=18,
                        padding=5,
                        display_format="{updates} ",
                        no_update_string="",
                        update_interval=3600,
                        distro="Arch_checkupdates"
                    ),
                    widget.Systray(
                        background=theme['Acolor0'],
                        icon_size=20,
                        padding=5
                    ),
                    get_separator(),
                    widget.TextBox(
                        background=theme['Gcolor0'],
                        fmt="   {} ",
                        text="ENG",
                        mouse_callbacks={
                            "Button1": change_keymap
                        }
                    ),
                    get_separator(),
                    widget.Volume(
                        background=theme['Bcolor0'],
                        fmt="   {} "
                    ),
                    get_separator(),
                    widget.TextBox(text=" "),
                    widget.Battery(
                        format="{char} {percent:2.0%}",
                        charge_char="",
                        discharge_char="",
                        empty_char="",
                        full_char="F",
                        update_interval=5,
                    ),
                    arcobattery.BatteryIcon(
                        padding=-1,
                        scale=0.8,
                        y_poss=1,
                        scaleadd=1,
                        theme_path=HOME +
                        ".config/qtile/resources/battery_icons_horiz",
                        update_interval=5,
                    ),
                    widget.TextBox(text=" ")
                ],
                20, border_color=theme['Wcolor1'], border_width=[0, 0, 1, 0],
                opacity=0.9
            ),
            bottom=bar.Bar(
                [
                    get_separator(),
                    widget.CurrentLayoutIcon(
                        background=theme['Ycolor0'],
                        scale=0.8,
                        fontsize=20,
                        padding=5,
                    ),
                    get_separator(),
                    widget.WindowName(
                        fontsize=15,
                        padding=5,
                        fmt=" {}"
                    ),
                    get_separator(),
                    widget.Clock(
                        background=theme['Mcolor0'],
                        format='  %d/%m/%Y   %H:%M ',
                        font=default_font_bold,
                    ),
                    get_separator(),
                    widget.TextBox(
                        background=theme['Rcolor0'],
                        font='sans',
                        fontsize=20,
                        fmt="",
                        padding=5,
                        mouse_callbacks={
                            "Button1": lazy.spawn("oblogout")
                        }
                    ),
                ],
                16, border_color=theme['Wcolor1'], border_width=[1, 0, 0, 0],
                opacity=0.9
            ),
        ),
    ]
