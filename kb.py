import board
from digitalio import Pull

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.digitalio import MatrixScanner


class KMKKeyboard(_KMKKeyboard):
    row_pins = [getattr(board, f"GP{row}") for row in (8, 6, 19, 20, 18)]
    col_pins = [getattr(board, f"GP{col}") for col in (26, 27, 4, 5, 1, 23, 22, 21, 28, 3, 7, 12, 13, 14, 15)]
    diode_orientation = DiodeOrientation.ROW2COL
    rgb_pixel_pin = board.GP2
    num_pixels = 75
    disable_auto_write = False
    brightness_limit = 0.5
    brightness_step = 0.025
    led_key_pos = list(range(75))

    def __init__(self):
        # create and register the scanner
        self.matrix = MatrixScanner(
            self.col_pins,
            self.row_pins,
            diode_orientation=self.diode_orientation,
            pull=Pull.DOWN,
            rollover_cols_every_rows=None,
            offset=0,
        )
