import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.BUTTON,
    storage=False,
    usb_id=('KMK Keyboards', 'Ferris Sweep'),
)

