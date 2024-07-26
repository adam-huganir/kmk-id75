from kb import KMKKeyboard
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_rgb_matrix import Color, Rgb_matrix
from kmk.modules.capsword import CapsWord
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.tapdance import TapDance

    # make sure our key extension modules are loaded

MODULES = (CapsWord(), Layers(), MouseKeys(), HoldTap(), TapDance())
EXTENSIONS = (MediaKeys(), Rgb_matrix(ledDisplay=75 * [Color.PURPLE]))
keyboard = KMKKeyboard()
keyboard.modules.extend(MODULES)
keyboard.extensions.extend(EXTENSIONS)

from keymaps import adam

keyboard.keymap = adam

if __name__ == "__main__":
    keyboard.debug_enabled = True
    keyboard.go()
