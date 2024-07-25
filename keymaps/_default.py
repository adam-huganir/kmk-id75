from kmk.keys import KC

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
        ____,      ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,       ____,
        ____,      ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,       ____,
        ____,      ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    "RGB_TOG",  ____,
        ____,      ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    "RGB_BRI",  ____,
        ____,      ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    "RGB_BRD",  ____,
   ],

]
# fmt:on

for layer in keymaps:
    for idx, key in enumerate(layer):
        layer[idx] = KC[key] if isinstance(key, str) else key
