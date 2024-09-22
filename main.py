# Replicates default Ferris keymap from QMK
# Credit: Pierre Chevalier, 2020
# https://github.com/qmk/qmk_firmware/tree/master/keyboards/ferris/keymaps/default

import board

from kb import KMKKeyboard

from kmk.extensions.rgb import RGB
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.split import Split

import keymap

keyboard = KMKKeyboard()

# split_side = SplitSide.LEFT
# split_side = SplitSide.RIGHT
split_side = None  # auto-detect based on drive name
split = Split(
    data_pin=board.D1,
    split_side=split_side,
    split_target_left=True,
    use_pio=True,
    uart_flip=True,
)

holdtap = HoldTap()
mouse_key = MouseKeys()

# fmt: off
NEOPIXEL_OFF = (0, 0, 0)
layer_to_color = {
    0: NEOPIXEL_OFF,        # QWERTY
    1: (  50, 150, 250),    # MOUSE
    2: ( 255, 215,   0),    # NAVIGATION
    3: ( 255, 100, 100),    # RIGHT SYMBOLS
    4: ( 255, 165,   0),    # LEFT SYMBOLS
    5: (  75,   0, 130),    # FUNCTIONS
    6: ( 255, 192, 203),    # NUMBERS
    7: ( 128,   0, 128),    # ALWAYS AVAILABLE
}
# fmt: on


class LayerRGB(RGB):
    def on_layer_change(self, layer):
        self.set_rgb_fill(layer_to_color.get(layer, NEOPIXEL_OFF))
        self.show()


rgb = LayerRGB(
    pixel_pin=board.NEOPIXEL,
    num_pixels=1,
    hue_default=0,
    sat_default=0,
    val_default=0,
)
keyboard.extensions.append(rgb)


class RGBLayers(Layers):
    def activate_layer(self, keyboard, layer, idx=None):
        super().activate_layer(keyboard, layer, idx)
        rgb.on_layer_change(layer)

    def deactivate_layer(self, keyboard, layer):
        super().deactivate_layer(keyboard, layer)
        rgb.on_layer_change(keyboard.active_layers[0])


layers = RGBLayers()

keyboard.modules = [
    layers,
    RGBLayers(),
    split,
    holdtap,
    mouse_key,
]

keymap.apply(keyboard)

if __name__ == "__main__":
    keyboard.go()
