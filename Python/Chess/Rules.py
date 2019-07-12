# y - Up/Down
# y - Left/Right

import GameElements as GE


class CanMove(object):
    canMoveFigure = []
    boardGr = []

    def __init__(self, x, y, board, allOponentPosToAttak = []):
        self.board = board
        item = board.boardGraphic[x][y]
        img = item.img
        color = item.color
        self.allOponentPosToAttak = allOponentPosToAttak
        self.canMove = self.CheckUniteMoves(x, y, img, color)

    def __repr__(self):
        return self.canMove

    def Vizualize(self):
        for item in self.canMove:
            self.board.boardGraphic[item[0]][item[1]] = "▢ "

        ret = ''
        for y in range(8):
            ret += '{number} '.format(number=8 - y) + \
                   ''.join(map(str, self.board.boardGraphic[7 - y])) + "\n"
        ret += "  a b c d e f g h\n"
        return ret

    def CheckUniteMoves(self, x, y, img, color):
        if img == ['♔ ', '♚ ']:
            return self.__King(x, y, color)
        elif img == ['♕ ', '♛ ']:
            return self.__Queen(x, y, color)
        elif img == ['♖ ', '♜ ']:
            return self.__Rook(x, y, color)
        elif img == ['♗ ', '♝ ']:
            return self.__Bishop(x, y, color)
        elif img == ['♘ ', '♞ ']:
            return self.__Knight(x, y, color)
        elif img == ['♙ ', '♟ ']:
            return self.__Pawn(x, y, color)
        else:
            return []

    @staticmethod
    def CheckPositionToOpponentUnit(x, y, color, board):
        canMoveFigure = ['♛ ', '♚ ', '♝ ', '♞ ', '♜ ', '♟ '] if color == 0 \
            else ['♙ ', '♖ ', '♘ ', '♗ ', '♔ ', '♕ ']
        if 0 <= x < 8 and 0 <= y < 8:
            bool = str(board.boardGraphic[x][y]) in canMoveFigure
            return bool

    @staticmethod
    def CheckPositionToVoid(x, y, board):
        # print(Board.GetBoardGraphic[x][y] == "• ")
        if 0 <= x < 8 and 0 <= y < 8:
            return board.boardGraphic[x][y] == "• "

    def CheckPositionToNotAttack(self, x, y):
        # print(Board.GetBoardGraphic[x][y] == "• ")
        if 0 <= x < 8 and 0 <= y < 8:
            return not (x, y) in self.allOponentPosToAttak

    def __King(self, x, y, color):
        canMove = []

        positionToMove = [(x+1, y-1), (x+1, y), (x+1, y+1),
                          (x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1), (x, y-1)]

        for item in positionToMove:
            if (self.CheckPositionToOpponentUnit(item[0], item[1], color, self.board) or self.CheckPositionToVoid(item[0], item[1], self.board)) and self.CheckPositionToNotAttack(item[0], item[1]):
                canMove += [(item[0], item[1],)]

        return canMove

    def __Queen(self, x, y, color):
        return self.__Rook(x, y, color) + self.__Bishop(x, y, color)

    def __Rook(self, x, y, color):

        canMove = []
        for i in range(1, 8):
            if self.CheckPositionToVoid(x + i, y, self.board):
                canMove += [(x + i, y)]
            elif self.CheckPositionToOpponentUnit(x + i, y, color, self.board):
                canMove += [(x + i, y)]
                break
            else:
                break

        for i in range(1, 8):
            if self.CheckPositionToVoid(x - i, y, self.board):
                canMove += [(x - i, y)]
            elif self.CheckPositionToOpponentUnit(x - i, y, color, self.board):
                canMove += [(x - i, y)]
                break
            else:
                break

        for i in range(1, 8):
            if self.CheckPositionToVoid(x, y + i, self.board):
                canMove += [(x, y + i)]
            elif self.CheckPositionToOpponentUnit(x, y + i, color, self.board):
                canMove += [(x, y + i)]
                break
            else:
                break

        for i in range(1, 8):
            if self.CheckPositionToVoid(x, y - i, self.board):
                canMove += [(x, y - i)]
            elif self.CheckPositionToOpponentUnit(x, y - i, color, self.board):
                canMove += [(x, y - i)]
                break
            else:
                break

        return canMove

    def __Bishop(self, x, y, color):
        canMove = []
        for i in range(1, 8):
            if self.CheckPositionToVoid(x + i, y + i, self.board):
                canMove += [(x + i, y + i)]
            elif self.CheckPositionToOpponentUnit(x + i, y + i, color, self.board):
                canMove += [(x + i, y + i)]
                break
            else:
                break

        for i in range(1, 8):
            if self.CheckPositionToVoid(x - i, y - i, self.board):
                canMove += [(x - i, y - i)]
            elif self.CheckPositionToOpponentUnit(x - i, y - i, color, self.board):
                canMove += [(x - i, y - i)]
                break
            else:
                break

        for i in range(1, 8):
            if self.CheckPositionToVoid(x - i, y + i, self.board):
                canMove += [(x - i, y + i)]
            elif self.CheckPositionToOpponentUnit(x - i, y + i, color, self.board):
                canMove += [(x - i, y + i)]
                break
            else:
                break

        for i in range(1, 8):
            if self.CheckPositionToVoid(x + i, y - i, self.board):
                canMove += [(x + i, y - i)]
            elif self.CheckPositionToOpponentUnit(x + i, y - i, color, self.board):
                canMove += [(x + i, y - i)]
                break
            else:
                break

        return canMove

    def __Knight(self, x, y, color):
        canMove = []

        positionToMove = [(x+2, y+1), (x+2, y-1), (x-2, y+1),
                          (x-2, y-1), (x+1, y+2), (x-1, y+2), (x+1, y-2), (x-1, y-2)]

        for item in positionToMove:
            if self.CheckPositionToOpponentUnit(item[0], item[1], color, self.board) or self.CheckPositionToVoid(item[0], item[1], self.board):
                canMove += [(item[0], item[1],)]
        return canMove

    def __Pawn(self, x, y, color):
        canMove = []

        if color == 0:
            if self.CheckPositionToVoid(x+1, y, self.board):
                canMove += [(x+1, y,)]
                if x == 1 and self.CheckPositionToVoid(x+2, y, self.board):
                    canMove += [(x+2, y)]
            if self.CheckPositionToOpponentUnit(x+1, y+1, color, self.board):
                canMove += [(x+1, y+1)]
            if self.CheckPositionToOpponentUnit(x+1, y-1, color, self.board):
                canMove += [(x+1, y-1)]
        else:
            if self.CheckPositionToVoid(x-1, y, self.board):
                canMove += [(x-1, y,)]
                if x == 6 and self.CheckPositionToVoid(x-2, y, self.board):
                    canMove += [(x-2, y)]
            if self.CheckPositionToOpponentUnit(x-1, y+1, color, self.board):
                canMove += [(x-1, y+1)]
            if self.CheckPositionToOpponentUnit(x-1, y-1, color, self.board):
                canMove += [(x-1, y-1)]

        return canMove
