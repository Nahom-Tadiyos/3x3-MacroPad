from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation, MatrixScanner
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.rotary import RotaryEncoder
import board

keyboard = KMKKeyboard()

cols = [board.D4, board.D5, board.D6]
rows = [board.D11, board.D12, board.D13]

scanner = MatrixScanner(
    row_pins=rows,
    col_pins=cols,
    diode_orientation=DiodeOrientation.COL2ROW
)

keyboard.modules.append(scanner)

keyboard.extensions.append(MediaKeys())

encoder = RotaryEncoder(
    pins=(board.D3, board.D2),
    clockwise=KC.VOLU,
    counter_clockwise=KC.VOLD,
    button=board.D1,
    button_key=KC.ENTER
)

keyboard.modules.append(encoder)

keyboard.keymap = [
    [
        [KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.T)],
        [KC.N1, KC.N2, KC.N3],
        [KC.N4, KC.N5, KC.N6],
    ]
]

if __name__ == "__main__":
    keyboard.go()