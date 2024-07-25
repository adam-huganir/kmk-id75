import board

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard


class KMKKeyboard(_KMKKeyboard):
    row_pins = [getattr(board, f"GP{row}") for row in (8, 6, 19, 20, 18)]
    col_pins = [getattr(board, f"GP{col}") for col in (26, 27, 4, 5, 1, 23, 22, 21, 28, 3, 7, 12, 13, 14, 15)]
    diode_orientation = DiodeOrientation.ROW2COL


keyboard = KMKKeyboard()
layers = Layers()
keyboard.modules.extend((layers,))

# fmt: off
keyboard.keymap = keymaps = [
    [
        KC.ESC,     KC.N1,    KC.N2,    KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,    KC.N9,    KC.N0,    KC.MINS,  KC.EQL,   KC.BSLS, KC.GRV,
        KC.TAB,     KC.Q,     KC.W,     KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,     KC.O,     KC.P,     KC.LBRC,  KC.RBRC,  KC.BSPC, KC.DEL,
        KC.CAPS,    KC.A,     KC.S,     KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,     KC.L,     KC.SCLN,  KC.QUOT,  KC.ENT,   KC.ENT,  KC.PGUP,
        KC.LSHIFT,  KC.Z,     KC.X,     KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM,  KC.DOT,   KC.SLSH,  KC.RSFT,  KC.RSFT,  KC.UP,   KC.PGDN,
        KC.LCTL,    KC.LGUI,  KC.LALT,  KC.SPC,  KC.SPC,  KC.SPC,  KC.SPC,  KC.SPC,  KC.SPC,  KC.RALT,   KC.RCTL,  KC.RCTL,  KC.LEFT,  KC.DOWN, KC.RGHT,
   ],
]
# fmt: on

if __name__ == "__main__":
    keyboard.debug_enabled = True
    keyboard.go()
