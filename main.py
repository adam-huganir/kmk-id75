from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
layers = Layers()
keyboard.modules.append(layers)

# Key aliases
______ = KC.TRNS
XXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)

# fmt:off
keymaps = [
    [
        "ESC",       "N1",      "N2",      "N3",     "N4",     "N5",     "N6",     "N7",     "N8",      "N9",      "N0",       "MIN",      "EQ",       "BKSP",    "DEL",
        "TAB",       "Q",       "W",       "E",      "R",      "T",      "Y",      "U",      "I",       "O",       "P",        "LBRKT",    "RBRKT",    "BKSP",    "DEL",
        "CAPS",      "A",       "S",       "D",      "F",      "G",      "H",      "J",      "K",       "L",       "SCLN",     "QUOT",     "ENT",      "ENT",     "PGUP",
        "LSHIFT",    "Z",       "X",       "C",      "V",      "B",      "N",      "M",      "COMM",    "DOT",     "SLSH",     "RSFT",     "RSFT",     "UP",      "PGDN",
        "LCTL",      "LGUI",    "LALT",    "SPC",    "SPC",    "SPC",    "SPC",    "SPC",    "RALT",    "RGUI",    "RCTL",     "MO",       "LEFT",     "DOWN",    "RGHT",

    ],
]
# fmt:on

for layer in keymaps:
    for idx, key in enumerate(layer):
        layer[idx] = KC[key]
keyboard.keymap = keymaps

if __name__ == "__main__":
    keyboard.debug_enabled = True
    keyboard.go()
