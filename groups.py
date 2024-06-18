from libqtile.config import Group

types = {
        'icons': ["", "", "", "", "", "", "", "", "", ""],
        'numbers': ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
        }


def init_groups(kind) -> list[Group]:
    groups = []
    groups = [Group(i) for i in types[kind]]
    return groups
