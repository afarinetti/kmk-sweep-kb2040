# Based on: https://github.com/manna-harbour/miryoku_kmk/blob/main/src/build/main.py

from kb import KMKKeyboard
from kmk.keys import KC, Key
from kmk.modules.capsword import CapsWord
from kmk.modules.power import Power
from kmk.modules.tapdance import TapDance


def HT(key_tap: Key, key_hold: Key) -> Key:
    return KC.HT(key_tap, key_hold, prefer_hold=False, tap_interrupted=True, tap_time=200)


def LT(key_tap: Key, key_hold: Key) -> Key:
    return KC.LT(key_tap, key_hold, prefer_hold=True, tap_interrupted=False, tap_time=200)


def TD(key_tap: Key, key_tap_dance: Key) -> Key:
    return KC.TD(key_tap, key_tap_dance, tap_time=200)


def TD_NO(key_tap_dance: Key) -> Key:
    return TD(KC.NO, key_tap_dance)


def apply(keyboard: KMKKeyboard):
    # combo_layers = {
    #     (4, 5): 6,
    #     (8, 7): 9,
    # }
    # keyboard.modules.append(Layers(combo_layers))

    keyboard.modules.extend(
        [
            TapDance(),
            Power(),
            # MediaKeys(),
            CapsWord(),
        ]
    )

    HT_A_LGUI = HT(KC.A, KC.LGUI)
    HT_R_LALT = HT(KC.R, KC.LALT)
    HT_S_LCTL = HT(KC.S, KC.LCTL)
    HT_T_LSFT = HT(KC.T, KC.LSFT)

    HT_N_SHFT = HT(KC.A, KC.LSFT)
    HT_E_LCTL = HT(KC.R, KC.LCTL)
    HT_I_LALT = HT(KC.S, KC.LALT)
    HT_O_LGUI = HT(KC.T, KC.LGUI)

    LT_3_Z = LT(3, KC.Z)
    # HT_X_RALT = HT(KC.X, KC.RALT)
    # HT_DOT_RALT = HT(KC.DOT, KC.RALT)
    LT_3_SLSH = LT(3, KC.SLSH)

    # fmt: off
    keyboard.keymap = [
        # BASE - 0
        [
            KC.Q,       KC.W,       KC.F,       KC.P,       KC.B,       KC.J,       KC.L,       KC.U,       KC.Y,       KC.QUOT,
            HT_A_LGUI,  HT_R_LALT,  HT_S_LCTL,  HT_T_LSFT,  KC.G,       KC.M,       HT_N_SHFT,  HT_E_LCTL,  HT_I_LALT,  HT_O_LGUI,
            LT_3_Z,     KC.X,       KC.C,       KC.D,       KC.V,       KC.K,       KC.H,       KC.COMM,    KC.DOT,     LT_3_SLSH,
                                            LT(4, KC.SPC), LT(5, KC.TAB), LT(8, KC.ENT), LT(7, KC.BSPC),
        ],
        # EXTRA - 1
        [
            KC.Q,
            KC.W,
            KC.E,
            KC.R,
            KC.T,
            KC.Y,
            KC.U,
            KC.I,
            KC.O,
            KC.P,

            HT(KC.A, KC.LGUI),
            HT(KC.S, KC.LALT),
            HT(KC.D, KC.LCTL),
            HT(KC.F, KC.LSFT),
            KC.G,
            KC.H,
            HT(KC.J, KC.LSFT),
            HT(KC.K, KC.LCTL),
            HT(KC.L, KC.LALT),
            HT(KC.QUOT, KC.LGUI),

            LT(3, KC.Z),
            HT(KC.X, KC.RALT),
            KC.C,
            KC.V,
            KC.B,
            KC.N,
            KC.M,
            KC.COMM,
            HT(KC.DOT, KC.RALT),
            LT(3, KC.SLSH),

            # LT(6, KC.ESC),  # TODO: Ferris Seep does not have this key (use combo layers)
            LT(4, KC.SPC),
            LT(5, KC.TAB),

            LT(8, KC.ENT),
            LT(7, KC.BSPC),
            # LT(9, KC.DEL),  # TODO: Ferris Sweep does not have this key (use combo layers)
        ],
        # TAP - 2
        [
            KC.Q,       KC.W,       KC.F,       KC.P,       KC.B,       KC.J,       KC.L,       KC.U,       KC.Y,       KC.QUOT,
            KC.A,       KC.R,       KC.S,       KC.T,       KC.G,       KC.M,       KC.N,       KC.E,       KC.I,       KC.O,
            KC.Z,       KC.X,       KC.C,       KC.D,       KC.V,       KC.K,       KC.H,       KC.COMM,    KC.DOT,     KC.SLSH,
                                                KC.SPC,     KC.TAB,     KC.ENT,     KC.BSPC,
        ],
        # BUTTON - 3
        [
            KC.NO,              KC.LSFT(KC.DEL),    KC.LCTL(KC.INS),    KC.LSFT(KC.INS),    KC.NO,              KC.NO,              KC.LSFT(KC.INS),    KC.LCTL(KC.INS),    KC.LSFT(KC.DEL),    KC.NO,
            KC.LGUI,            KC.LALT,            KC.LCTL,            KC.LSFT,            KC.NO,              KC.NO,              KC.LSFT,            KC.LCTL,            KC.LALT,            KC.LGUI,
            KC.NO,              KC.LSFT(KC.DEL),    KC.LCTL(KC.INS),    KC.LSFT(KC.INS),    KC.NO,              KC.NO,              KC.LSFT(KC.INS),    KC.LCTL(KC.INS),    KC.LSFT(KC.DEL),    KC.NO,
                                                                        KC.MB_LMB,          KC.MB_RMB,          KC.MB_RMB,          KC.MB_LMB,
        ],
        # NAV - 4
        [
            TD_NO(KC.RELOAD),
            TD_NO(KC.DF(2)),
            TD_NO(KC.DF(1)),
            TD_NO(KC.DF(0)),
            KC.NO,
            KC.NO,
            KC.LSFT(KC.INS),
            KC.LCTL(KC.INS),
            KC.LSFT(KC.DEL),
            KC.NO,

            KC.LGUI,
            KC.LALT,
            KC.LCTL,
            KC.LSFT,
            KC.NO,
            TD(KC.CW, KC.CAPS),
            KC.LEFT,
            KC.DOWN,
            KC.UP,
            KC.RGHT,

            KC.NO,
            KC.RALT,
            TD_NO(KC.DF(7)),
            TD_NO(KC.DF(4)),
            KC.NO,
            KC.INS,
            KC.HOME,
            KC.PGDN,
            KC.PGUP,
            KC.END,

            # KC.NO,  # TODO: Ferris Sweep does not have this key
            KC.NO,
            KC.NO,
            KC.ENT,
            KC.BSPC,
            # KC.DEL,  # TODO: Ferris Sweep does not have this key
        ],
        # MOUSE - 5
        [
            TD_NO(KC.RELOAD),
            TD_NO(KC.DF(2)),
            TD_NO(KC.DF(1)),
            TD_NO(KC.DF(0)),
            KC.NO,
            KC.NO,
            KC.LSFT(KC.INS),
            KC.LCTL(KC.INS),
            KC.LSFT(KC.DEL),
            KC.NO,

            KC.LGUI,
            KC.LALT,
            KC.LCTL,
            KC.LSFT,
            KC.NO,
            KC.NO,
            KC.MS_LT,
            KC.MS_DN,
            KC.MS_UP,
            KC.MS_RT,

            KC.NO,
            KC.RALT,
            TD_NO(KC.DF(8)),
            TD_NO(KC.DF(5)),
            KC.NO,
            KC.NO,
            KC.NO,
            KC.MW_DN,
            KC.MW_UP,
            KC.NO,

            # KC.NO,  # TODO: Ferris Sweep does not have this key
            KC.NO,
            KC.NO,
            KC.MB_RMB,
            KC.MB_LMB,
            # KC.MB_MMB,  # TODO: Ferris Sweep does not have this key
        ],
        # MEDIA - 6
        [
            TD_NO(KC.RELOAD),
            TD_NO(KC.DF(2)),
            TD_NO(KC.DF(1)),
            TD_NO(KC.DF(0)),
            KC.NO,
            KC.NO,
            KC.NO,
            KC.NO,
            KC.NO,
            KC.NO,

            KC.LGUI,
            KC.LALT,
            KC.LCTL,
            KC.LSFT,
            KC.NO,
            KC.PS_TOG,
            KC.MPRV,
            KC.VOLD,
            KC.VOLU,
            KC.MNXT,
            
            KC.NO,
            KC.RALT,
            TD_NO(KC.DF(9)),
            TD_NO(KC.DF(6)),
            KC.NO,
            KC.HID,
            KC.NO,
            KC.NO,
            KC.NO,
            KC.NO,
            
            # KC.NO,  # TODO: Ferris Sweep does not have this key
            KC.NO,
            KC.NO,
            KC.MSTP,
            KC.MPLY,
            # KC.MUTE,  # TODO: Ferris Sweep does not have this key
        ],
        # NUM - 7
        [
            KC.LBRC,            KC.N7,              KC.N8,              KC.N9,              KC.RBRC,            KC.NO,              TD_NO(KC.DF(0)),    TD_NO(KC.DF(1)),    TD_NO(KC.DF(2)),    TD_NO(KC.RELOAD),
            KC.SCLN,            KC.N4,              KC.N5,              KC.N6,              KC.EQL,             KC.NO,              KC.LSFT,            KC.LCTL,            KC.LALT,            KC.LGUI,
            KC.GRV,             KC.N1,              KC.N2,              KC.N3,              KC.BSLS,            KC.NO,              TD_NO(KC.DF(7)),    TD_NO(KC.DF(4)),    KC.RALT,            KC.NO,
                                                                        KC.N0,              KC.MINS,            KC.NO,              KC.NO,
        ],
        # SYM - 8
        [
            KC.LCBR,
            KC.AMPR,
            KC.ASTR,
            KC.LPRN,
            KC.RCBR,
            KC.NO,
            TD_NO(KC.DF(0)),
            TD_NO(KC.DF(1)),
            TD_NO(KC.DF(2)),
            TD_NO(KC.RELOAD),

            KC.COLN,
            KC.DLR,
            KC.PERC,
            KC.CIRC,
            KC.PLUS,
            KC.NO,
            KC.LSFT,
            KC.LCTL,
            KC.LALT,
            KC.LGUI,

            KC.TILD,
            KC.EXLM,
            KC.AT,
            KC.HASH,
            KC.PIPE,
            KC.NO,
            TD_NO(KC.DF(8)),
            TD_NO(KC.DF(5)),
            KC.RALT,
            KC.NO,
            
            # KC.LPRN,  # TODO: Ferris Sweep does not have this key
            KC.RPRN,
            KC.UNDS,
            KC.NO,
            KC.NO,
            # KC.NO,  # TODO: Ferris Sweep does not have this key
        ],
        # FUN - 9
        [
            KC.F12,
            KC.F7,
            KC.F8,
            KC.F9,
            KC.PSCR,
            KC.NO,
            TD_NO(KC.DF(0)),
            TD_NO(KC.DF(1)),
            TD_NO(KC.DF(2)),
            TD_NO(KC.RELOAD),

            KC.F11,
            KC.F4,
            KC.F5,
            KC.F6,
            KC.SLCK,
            KC.NO,
            KC.LSFT,
            KC.LCTL,
            KC.LALT,
            KC.LGUI,

            KC.F10,
            KC.F1,
            KC.F2,
            KC.F3,
            KC.PAUS,
            KC.NO,
            TD_NO(KC.DF(9)),
            TD_NO(KC.DF(6)),
            KC.RALT,
            KC.NO,

            # KC.APP,  # TODO: Ferris Sweep does not have this key
            KC.SPC,
            KC.TAB,
            KC.NO,
            KC.NO,
            # KC.NO,  # TODO: Ferris Sweep does not have this key
        ],
    ]
    # fmt: off

layer_names_list = [
    "Base",
    "Extra",
    "Tap",
    "Button",
    "Nav",
    "Mouse",
    "Media",
    "Num",
    "Sym",
    "Fun",
]
