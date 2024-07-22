import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    row_pins = [getattr(board, f"GP{row}") for row in (8, 6, 19, 20, 18)]
    col_pins = [getattr(board, f"GP{col}") for col in (26, 27, 4, 5, 1, 23, 22, 21, 28, 3, 7, 12, 13, 14, 15)]
    diode_orientation = DiodeOrientation.ROW2COL
    rgb_pixel_pin = board.GP2
    num_pixels = 75
    disable_auto_write = False
    brightness_limit = 1.0
    led_key_pos = list(range(75))
