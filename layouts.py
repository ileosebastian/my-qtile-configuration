from libqtile import layout


def init_layouts(defaut_layouts):
    return [
        layout.Columns(**defaut_layouts),
        layout.Max(**defaut_layouts),
        layout.TreeTab(**defaut_layouts)
    ]
