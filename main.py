import board

from kb import KMKKeyboard, # Rgb_matrix
# from kmk.extensions.peg_rgb_matrix import Color
# from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
# layers = Layers()
# rgb = Rgb_matrix(
#     rgb_pixel_pin=board.GP2,
#     num_pixels=75,
#     disable_auto_write=False,
#     brightness_limit=0.25,
#     led_key_pos=list(range(75)),
#     led_display=75 * [Color.PURPLE],
# )
# keyboard.modules.extend((layers,))
# keyboard.extensions.extend((rgb,))

from keymaps import default # noqa:  E402

keyboard.keymap = default

if __name__ == "__main__":
    keyboard.debug_enabled = True
    keyboard.go()
