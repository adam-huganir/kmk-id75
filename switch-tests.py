import board
import digitalio

rows = [digitalio.DigitalInOut(getattr(board, f"GP{x}")) for x in (8, 6, 19, 20, 18)]
cols = [digitalio.DigitalInOut(getattr(board, f"GP{x}")) for x in (26, 27, 4, 5, 1, 23, 22, 21, 28, 3, 7, 12, 13, 14, 15)]


for c in cols:
    c.direction = digitalio.Direction.INPUT
    c.pull = digitalio.Pull.DOWN

for r in rows:
    r.direction = digitalio.Direction.OUTPUT
    r.value = False

pressed = {(r, c): False for r in range(len(rows)) for c in range(len(cols))}
while True:
    for row_i in range(len(rows)):
        for col_i in range(len(cols)):
            rows[row_i].value = True
            if cols[col_i].value and not pressed[(row_i, col_i)]:
                    print(f"Row {row_i}, Col {col_i} pressed")
                    pressed[(row_i, col_i)] = True
            elif not cols[col_i].value and pressed[(row_i, col_i)]:
                print(f"Row {row_i}, Col {col_i} released")
                pressed[(row_i, col_i)] = False
            rows[row_i].value = False