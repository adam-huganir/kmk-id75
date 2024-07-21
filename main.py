from kb import KMKKeyboard, Rgb_matrix
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.peg_rgb_matrix import Color

keyboard = KMKKeyboard()
layers = Layers()
rgb = Rgb_matrix(ledDisplay=75 * [Color.WHITE] + 14 * [Color.OFF])
keyboard.modules.append(layers)
keyboard.extensions.append(rgb)

# Key aliases
____ = KC.TRNS
XXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)

# fmt:off
keymaps = [
    [
        "ESC",     "N1",    "N2",    "N3",   "N4",   "N5",   "N6",   "N7",   "N8",    "N9",    "N0",    "MINS",  "EQL",   "BSLS", "GRV",
        "TAB",     "Q",     "W",     "E",    "R",    "T",    "Y",    "U",    "I",     "O",     "P",     "LBRC",  "RBRC",  "BSPC", "DEL",
        "CAPS",    "A",     "S",     "D",    "F",    "G",    "H",    "J",    "K",     "L",     "SCLN",  "QUOT",  "ENT",   "ENT",  "PGUP",
        "LSHIFT",  "Z",     "X",     "C",    "V",    "B",    "N",    "M",    "COMM",  "DOT",   "SLSH",  "RSFT",  LOWER,   "UP",   "PGDN",
        "LCTL",    "LGUI",  "LALT",  "SPC",  "SPC",  "SPC",  "SPC",  "SPC",  "SPC",  "RALT",   "RCTL",  "RCTL",  "LEFT",  "DOWN", "RGHT",
   ],
        [
        "RGB_BRI", ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,
        "RGB_BRD", ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,
        "RGB_TOG", ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,
        ____,      ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,
        ____,      ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,
   ],

]
# fmt:on

for layer in keymaps:
    for idx, key in enumerate(layer):
        layer[idx] = KC[key] if isinstance(key, str) else key
keyboard.keymap = keymaps

if __name__ == "__main__":
    keyboard.debug_enabled = True
    keyboard.go()
