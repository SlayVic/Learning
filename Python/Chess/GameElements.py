class Board(object):
    boardGraphic = []

    def __init__(self, whiteFigures, blackFigures):
        self.boardGraphic = [["• "] * 8 for y in range(8)]
        self.SetFigures(whiteFigures, blackFigures)
        # self.setFigure(Pawn(1, 3, 2))
        # self.setFigure(Pawn(0, 2, 1))

    def SetFigures(self, whiteFigures, blackFigures):
        self.boardGraphic = [["• "] * 8 for y in range(8)]
        for figure in whiteFigures:
            self.setFigure(figure)
        for figure in blackFigures:
            self.setFigure(figure)

    def setFigure(self, figure):
        x = figure.x
        y = figure.y
        self.boardGraphic[x][y] = figure

    def __repr__(self):
        ret = ''
        for y in range(8):
            ret += '{number} '.format(number=8 - y) + \
                   ''.join(map(str, self.boardGraphic[7 - y])) + "\n"
        ret += "  a b c d e f g h\n"
        return ret

    def GetBoardGraphic(self):
        return self.boardGraphic


class ChessFigure(object):
    img = None

    def __init__(self, color, x, y):
        self.color = color
        self.x = x if x >= 0 else 8 + x
        self.y = y if y >= 0 else 8 + y

    def __repr__(self):
        return self.img[self.color]


class King(ChessFigure):
    img = ['♔ ', '♚ ']


class Queen(ChessFigure):
    img = ['♕ ', '♛ ']


class Rook(ChessFigure):
    img = ['♖ ', '♜ ']


class Bishop(ChessFigure):
    img = ['♗ ', '♝ ']


class Knight(ChessFigure):
    img = ['♘ ', '♞ ']


class Pawn(ChessFigure):
    img = ['♙ ', '♟ ']
