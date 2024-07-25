from kb import KMKKeyboard
from kmk.modules.layers import Layers
from kmk.extensions.peg_rgb_matrix import Color
from kmk.extensions.peg_rgb_matrix import Rgb_matrix

keyboard = KMKKeyboard()
layers = Layers()
rgb = Rgb_matrix(ledDisplay=75 * [Color.PURPLE])
keyboard.modules.append(layers)
keyboard.extensions.append(rgb)

from keymaps import default

keyboard.keymap = default

if __name__ == "__main__":
    keyboard.debug_enabled = True
    keyboard.go()
