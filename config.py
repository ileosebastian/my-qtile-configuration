# LIBRARIES
from typing import List  # noqa: F401
# My imports
from groups import init_groups
from keys import init_keys
from keys import init_const_mouse
from keys import group_types
from layouts import init_layouts
from screens import init_screens
from my_qtile_functions import autostart, restart_qtile
from my_qtile_functions import set_key_map
from rules import init_floating_layout
from theming import theme


PYTHONTRACEMALLOC = 1


# VARIABLE SETTINGS
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
kind = "numbers"

df_layouts = theme.layouts
# WIDGETS
widget_defaults = theme.widgets
extension_defaults = widget_defaults.copy()

# KEYS
keys = init_keys()
# Drag floating layouts.
mouse = init_const_mouse()

# GROUPS
groups = []
groups = init_groups(kind)
keys.extend(group_types(groups, kind))

# LAYOUTS
layouts = init_layouts(df_layouts)
floating_layout = init_floating_layout(df_layouts)

# SCREENS
screens = init_screens()

wmname = "LG3D"  # Neede for some Java apps: LG3D

# My Functions
restart_qtile()
set_key_map()
autostart()
