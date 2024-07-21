from time import sleep

import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard, debug_error
from kmk.scanners import DiodeOrientation
from kmk.extensions.peg_rgb_matrix import Rgb_matrix as _Rgb_matrix, Rgb_matrix_data as _Rgb_matrix_data


class KMKKeyboard(_KMKKeyboard):
    row_pins = [getattr(board, f"GP{row}") for row in (8, 6, 19, 20, 18)]
    col_pins = [getattr(board, f"GP{col}") for col in (26, 27, 4, 5, 1, 23, 22, 21, 28, 3, 7, 12, 13, 14, 15)]
    diode_orientation = DiodeOrientation.ROW2COL
    rgb_pixel_pin = board.GP2
    num_pixels = 89
    disable_auto_write = False
    brightness_limit = 1.0
    led_key_pos = list(range(89))

    def before_matrix_scan(self) -> None:
        for module in self.modules:
            try:
                module.before_matrix_scan(self)
            except Exception as err:
                debug_error(module, "before_matrix_scan", err)

        for ext in self.extensions:
            try:
                ext.before_matrix_scan(self.sandbox)
            except Exception as err:
                debug_error(ext, "before_matrix_scan", err)

class Rgb_matrix(_Rgb_matrix):
    def increase_brightness(self, step=None):

        for i, val in enumerate(self.ledDisplay):
            self.neopixel[self.keyPos[i]] = (0,0,0)
        for i, val in enumerate(self.ledDisplay):
            if i > 75:
                print(i)
                self.neopixel[self.keyPos[i]] = (val[0], val[1], val[2])
                sleep(1)