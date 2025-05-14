from chessPictures import square, rock, knight, bishop, queen, king, pawn
from interpreter import draw
from functools import reduce
from picture import Picture

# cuadros blanco y negro
white = square
black = square.negative()

# fila de casillas alternadas con piezas dentro
def make_row(pieces, start_with_white):
    row = []
    for i, piece in enumerate(pieces):
        cell = white if (i + start_with_white) % 2 == 0 else black
        row.append(cell.under(piece))  # la pieza dentro de la casilla
    return reduce(lambda acc, pic: acc.join(pic), row)

def make_empty_row(start_with_white):
    row = []
    for i in range(8):
        cell = white if (i + start_with_white) % 2 == 0 else black
        row.append(cell)
    return reduce(lambda acc, pic: acc.join(pic), row)

black_back_row = [rock, knight, bishop, queen, king, bishop, knight, rock]
black_pawn_row = [pawn] * 8

white_back_row = [p.negative() for p in black_back_row]
white_pawn_row = [p.negative() for p in black_pawn_row]


middle = (
    make_empty_row(0)
    .up(make_empty_row(1))
    .up(make_empty_row(0))
    .up(make_empty_row(1))
)

full_board = (
    make_row(black_back_row, 0)
    .up(make_row(black_pawn_row, 1))
    .up(middle)
    .up(make_row(white_pawn_row, 0))
    .up(make_row(white_back_row, 1))
)

# Mostramos el tablero con las piezas
draw(full_board)
