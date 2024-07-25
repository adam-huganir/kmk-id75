import board
import neopixel

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.extensions.peg_rgb_matrix import Rgb_matrix as _Rgb_matrix


class KMKKeyboard(_KMKKeyboard):
    row_pins = [getattr(board, f"GP{row}") for row in (8, 6, 19, 20, 18)]
    col_pins = [getattr(board, f"GP{col}") for col in (26, 27, 4, 5, 1, 23, 22, 21, 28, 3, 7, 12, 13, 14, 15)]
    diode_orientation = DiodeOrientation.ROW2COL


class Rgb_matrix(_Rgb_matrix):
    def __init__(
        self,
        rgb_order=(1, 0, 2),
        disable_auto_write=False,
        led_display=None,
        rgb_pixel_pin=board.GP2,
        num_pixels=75,
        brightness_limit=0.1,
        brightness_step=0.025,
        led_key_pos=None,
    ):
        if led_display is None:
            led_display = []
        super().__init__(rgb_order=rgb_order, disable_auto_write=disable_auto_write, ledDisplay=led_display)
        self.pin = rgb_pixel_pin
        self.num_pixels = num_pixels
        self.brightness_limit = brightness_limit
        self.led_key_pos = self.keyPos = led_key_pos or list(range(75))
        self.brightness_step = brightness_step
        self.neopixel = None

    def during_bootup(self, board):
        self.neopixel = neopixel.NeoPixel(
            self.pin,
            self.num_pixels,
            brightness=self.brightness_limit,
            pixel_order=self.rgb_order,
            auto_write=not self.disable_auto_write,
        )
        self.on()
        return
