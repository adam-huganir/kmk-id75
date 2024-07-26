from kmk.keys import KC


# Layers
LBAS = 0
LMED = 1
LNAV = 2
LMOU = 3
LSYM = 4
LNUM = 5
LFUN = 6

K = KC
XXX = K.NO
___ = K.TRNS

# Homerow mods
A_SUP = K.HT(K.A, K.LSUP)
R_ALT = K.HT(K.R, K.LALT)
S_CTL = K.HT(K.S, K.LCTL)
T_SFT = K.HT(K.T, K.LSFT)
N_SFT = K.HT(K.N, K.RSFT)
E_CTL = K.HT(K.E, K.RCTL)
I_ALT = K.HT(K.I, K.RALT)
O_SUP = K.HT(K.O, K.RSUP)

# Thumbs
SPC_NAV = K.LT(LBAS, K.SPC)
ESC_MED = K.LT(LMED, K.ESC)
TAB_MOU = K.LT(LMOU, K.TAB)
ENT_SYM = K.LT(LSYM, K.ENT)
BSPC_NUM = K.LT(LNUM, K.BSPC)
DEL_FUN = K.LT(LFUN, K.DEL)

# mod shortcuts
SH = K.SHIFT


layers = ["base", "media", "nav", "mouse", "symbol", "number", "function"]
# fmt: off
# "".join([cell.format(x) for x in range(15)]) + "|"
# |    0     |    1     |    2     |    3     |    4     |    5     |    6     |    7     |    8     |    9     |    10    |    11    |    12    |    13    |    14    |
KEYMAPS = {
"base":
    [
# |          |          |          |          |          |          |          |          |          |          |          |          |          |          |          |
   "ESC",     "N1",      "N2",      "N3",      "N4",      "N5",      XXX,       XXX,       "N6",      "N7",     "N8",       "N9",      "N0",      "GRV",     "HOME",
   "TAB",     "Q",       "W",       "F",       "P",       "B",       "COMM",    "DOT",     "J",       "L",      "U",        "Y",       "QUOT",    XXX,       "PGUP",
   "CAPS",    A_SUP,     R_ALT,     S_CTL,     T_SFT,     "G",       "LPRN",    "LPRN",    "M",       N_SFT,    E_CTL,      I_ALT,     O_SUP,     "QUOT",    "PGDN",
   "LSFT",    "Z",       "X",       "C",       "D",       "V",       "LBRC",    "RBRC",    "K",       "H",      "COMM",     "DOT",     "SLSH",    "UP",      "END",
   "LCTL",    "LGUI",    "LALT",    ESC_MED,   SPC_NAV,   TAB_MOU,   XXX,        XXX,      ENT_SYM,   BSPC_NUM,  DEL_FUN,   "RALT",    "LEFT",    "DOWN",    "RGHT"
    ],
"media":
    [
# |          |          |          |          |          |          |          |          |          |          |          |          |          |          |          |
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       "LGUI",    "LALT"     "LCTL",    "LSFT",    XXX,       XXX,       XXX,       "MPRV"     "VOLU",    "VOLD"     "MNXT",    XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       "MSTP",    "PLY",     "MUTE",    XXX,       XXX,       XXX,       XXX,
    ],
"nav":
     [
# |           |          |          |          |          |          |          |          |          |          |          |          |          |          |          |
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       "LGUI",    "LALT"     "LCTL",    "LSFT",    XXX,       XXX,       "CAPS",    "LEFT"     "DOWN",    "UP"       "RGHT",    XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       "INS",     "HOME"     "PGDN",    "PGUP"     "END",     XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       "ENT",     "BSPC",    "DEL",     XXX,       XXX,       XXX,       XXX,


    ],
"mouse":
    [
# |          |          |          |          |          |          |          |          |          |          |          |          |          |          |          |
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       "LGUI",    "LALT"     "LCTL",    "LSFT",    XXX,       XXX,       XXX,       "MS_LT",   "MS_DN",   "MS_UP",   "MS_RT",   XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       "MW_LT",   "MW_DN",   "MW_UP",   "MW_RT",   XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       "MB_RMB",  "MB_LMB",  "MB_MMB",  XXX,       XXX,       XXX,       XXX,       XXX,


    ],
"symbol":
    [
# |          |          |          |          |          |          |          |          |          |          |          |          |          |          |          |
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       "LABK",    "RABK",    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       "LPRN",    "RPRN",    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       "LBRC",    "RBRC",    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       "LCBR",    "RCBR",    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    ],
"number":
    [
# |          |          |          |          |          |          |          |          |          |          |          |          |          |          |          |
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    ],
"function":
    [
# |          |          |          |          |          |          |          |          |          |          |          |          |          |          |          |
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,       XXX,
    ],
}
# to format each block you can copy it and paste it into a interp as `block` and run:
#  for row in block.split("\n"):
#      print("".join([f"{k:11}" for k in re.split("\s{2,}", row)[1:15]]))
# fmt:on

for layer in KEYMAPS.values():
    for idx, key in enumerate(layer):
        layer[idx] = K[key] if isinstance(key, str) else key
keymaps = [KEYMAPS[layer] for layer in layers]