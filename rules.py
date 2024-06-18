from libqtile import layout
from libqtile.config import Match


def init_floating_layout(defaut_layouts):
    return layout.Floating(float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        Match(wm_class="oblogout"),
        Match(wm_class="notification"),
    ], **defaut_layouts)


# OLD config
def init_floating_layouts_():
    return layout.Floating(
            float_rules=[
                *layout.Floating.default_float_rules,
                Match(wm_class='confirmreset'),  # gitk
                Match(wm_class='makebranch'),  # gitk
                Match(wm_class='maketag'),  # gitk
                Match(wm_class='ssh-askpass'),  # ssh-askpass
                Match(title='branchdialog'),  # gitk
                Match(title='pinentry'),  # GPG key password entry
                Match(wm_class="oblogout"),
                Match(wm_class="notification"),
            ],
            border_focus=current_line,
            border_normal=comment,
            border_width=1
    )
