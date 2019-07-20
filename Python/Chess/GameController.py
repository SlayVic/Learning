import time

from Rules import CanMove
import GameElements as GE


class Controller(object):
    def __init__(self):
        self.whiteFigures = []
        for y in range(8):
            a = GE.Pawn(0, 1, y)
            self.whiteFigures.append(a)
        a = GE.Rook(0, 0, 0)
        self.whiteFigures.append(a)
        a = GE.Knight(0, 0, 1)
        self.whiteFigures.append(a)
        a = GE.Bishop(0, 0, 2)
        self.whiteFigures.append(a)
        a = GE.Queen(0, 0, 3)
        self.whiteFigures.append(a)
        a = GE.King(0, 0, 4)
        self.whiteFigures.append(a)
        a = GE.Bishop(0, 0, 5)
        self.whiteFigures.append(a)
        a = GE.Knight(0, 0, 6)
        self.whiteFigures.append(a)
        a = GE.Rook(0, 0, 7)
        self.whiteFigures.append(a)

        self.blackFigures = []

        for y in range(8):
            a = GE.Pawn(1, -2, y)
            self.blackFigures.append(a)
        a = GE.Rook(1, -1, 0)
        self.blackFigures.append(a)
        a = GE.Knight(1, -1, 1)
        self.blackFigures.append(a)
        a = GE.Bishop(1, -1, 2)
        self.blackFigures.append(a)
        a = GE.Queen(1, -1, 3)
        self.blackFigures.append(a)
        a = GE.King(1, -1, 4)
        self.blackFigures.append(a)
        a = GE.Bishop(1, -1, 5)
        self.blackFigures.append(a)
        a = GE.Knight(1, -1, 6)
        self.blackFigures.append(a)
        a = GE.Rook(1, -1, 7)
        self.blackFigures.append(a)

        self.queue = 0

        self.board = GE.Board(self.whiteFigures, self.blackFigures)

    def __repr__(self):
        pass

    # Сheck unite position to move
    def CheckUniteToMove(self, x, y, img, color):
        if img == ['♔ ', '♚ ']:
            return CanMove.__King(x, y, color)
        elif img == ['♕ ', '♛ ']:
            return CanMove.__Queen(x, y, color)
        elif img == ['♖ ', '♜ ']:
            return CanMove.__Rook(x, y, color)
        elif img == ['♗ ', '♝ ']:
            return CanMove.__Bishop(x, y, color)
        elif img == ['♘ ', '♞ ']:
            return CanMove.__Knight(x, y, color)
        elif img == ['♙ ', '♟ ']:
            return CanMove.__Pawn(x, y, color)
        else:
            return []

    def GetAllOponentPothitionToAttak(self):
        canMove = []
        retCanMove = []
        if self.queue == 0:
            for item in self.blackFigures:
                a = CanMove(item.x, item.y, self.board).canMove
                canMove.append(a)
        else:
            for item in self.whiteFigures:
                canMove.append(CanMove(item.x, item.y, self.board).canMove)

        for item in canMove:
            for cordinate in item:
                if not(cordinate in retCanMove):
                    retCanMove.append(cordinate)
        return retCanMove

    # Check. Can a pawn become a queen?
    def pawnToQuin(self):
        index = None
        for item in self.whiteFigures:
            if item.x == 7 and item.img == ['♙ ', '♟ ']:
                index = self.whiteFigures.index(item)
                self.whiteFigures.pop(index)
                self.whiteFigures.append(GE.Queen(0, 7, item.y))
            pass
        for item in self.blackFigures:
            if item.x == 0 and item.img == ['♙ ', '♟ ']:
                index = self.blackFigures.index(item)
                self.blackFigures.pop(index)
                self.blackFigures.append(GE.Queen(1, 0, item.y))

    def CheckToVoid(self, x, y):
        return self.board.boardGraphic[x][y] == "• "

    # Check. Is not a castling move?
    def Castling(self, moveFrom, moveTo):
        # Check white
        if self.queue == 0:
            # Cheak a1 Rook
            if (moveFrom[0], moveFrom[1]) == (0, 0) and self.board.boardGraphic[0][0].img == ['♖ ', '♜ ']:
                if (moveTo[0], moveTo[1]) == (0, 3) and self.board.boardGraphic[0][4].img == ['♔ ', '♚ ']:
                    if self.CheckToVoid(0, 1) and self.CheckToVoid(0, 2) and self.CheckToVoid(0, 3):
                        oponentCanMove = self.GetAllOponentPothitionToAttak()
                        if not (0, 2) in oponentCanMove and not (0, 4) in oponentCanMove:
                            moveFigureIndex = self.findFigure(
                                moveFrom[0], moveFrom[1], self.queue)
                            canMove = CanMove(
                                self.whiteFigures[moveFigureIndex].x, self.whiteFigures[moveFigureIndex].y, self.board, self.GetAllOponentPothitionToAttak()).canMove
                            if (moveTo[0], moveTo[1]) in canMove:
                                figure = self.whiteFigures.pop(moveFigureIndex)
                                figure.x = moveTo[0]
                                figure.y = moveTo[1]
                                self.whiteFigures.append(figure)
                                kingIndex = self.findFigure(0, 4, self.queue)
                                king = self.whiteFigures.pop(kingIndex)
                                king.x = 0
                                king.y = 2
                                self.whiteFigures.append(king)
                                self.queue = 1 if self.queue == 0 else 0
                                self.board.SetFigures(
                                    self.whiteFigures, self.blackFigures)
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            # Cheak h1 Rook
            elif (moveFrom[0], moveFrom[1]) == (0, 7) and self.board.boardGraphic[0][7].img == ['♖ ', '♜ ']:
                if (moveTo[0], moveTo[1]) == (0, 5) and self.board.boardGraphic[0][4].img == ['♔ ', '♚ ']:
                    if self.CheckToVoid(0, 6) and self.CheckToVoid(0, 5):
                        oponentCanMove = self.GetAllOponentPothitionToAttak()
                        if not (0, 6) in oponentCanMove and not (0, 4) in oponentCanMove:
                            moveFigureIndex = self.findFigure(
                                moveFrom[0], moveFrom[1], self.queue)
                            canMove = CanMove(
                                self.whiteFigures[moveFigureIndex].x, self.whiteFigures[moveFigureIndex].y, self.board, self.GetAllOponentPothitionToAttak()).canMove
                            if (moveTo[0], moveTo[1]) in canMove:
                                figure = self.whiteFigures.pop(moveFigureIndex)
                                figure.x = moveTo[0]
                                figure.y = moveTo[1]
                                self.whiteFigures.append(figure)
                                kingIndex = self.findFigure(0, 4, self.queue)
                                king = self.whiteFigures.pop(kingIndex)
                                king.x = 0
                                king.y = 6
                                self.whiteFigures.append(king)
                                self.queue = 1 if self.queue == 0 else 0
                                self.board.SetFigures(
                                    self.whiteFigures, self.blackFigures)
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        # Cheak black
        else:
            # Cheak a8 Rook
            if (moveFrom[0], moveFrom[1]) == (7, 0) and self.board.boardGraphic[7][0].img == ['♖ ', '♜ ']:
                if (moveTo[0], moveTo[1]) == (7, 3) and self.board.boardGraphic[7][4].img == ['♔ ', '♚ ']:
                    if self.CheckToVoid(7, 1) and self.CheckToVoid(7, 2) and self.CheckToVoid(7, 3):
                        oponentCanMove = self.GetAllOponentPothitionToAttak()
                        if not (7, 2) in oponentCanMove and not (7, 4) in oponentCanMove:
                            moveFigureIndex = self.findFigure(
                                moveFrom[0], moveFrom[1], self.queue)
                            canMove = CanMove(
                                self.blackFigures[moveFigureIndex].x, self.blackFigures[moveFigureIndex].y, self.board, self.GetAllOponentPothitionToAttak()).canMove
                            if (moveTo[0], moveTo[1]) in canMove:
                                figure = self.blackFigures.pop(moveFigureIndex)
                                figure.x = moveTo[0]
                                figure.y = moveTo[1]
                                self.blackFigures.append(figure)
                                kingIndex = self.findFigure(7, 4, self.queue)
                                king = self.blackFigures.pop(kingIndex)
                                king.x = 7
                                king.y = 2
                                self.blackFigures.append(king)
                                self.queue = 1 if self.queue == 0 else 0
                                self.board.SetFigures(
                                    self.whiteFigures, self.blackFigures)
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            # Cheak h1 Rook
            elif (moveFrom[0], moveFrom[1]) == (7, 7) and self.board.boardGraphic[7][7].img == ['♖ ', '♜ ']:
                if (moveTo[0], moveTo[1]) == (7, 5) and self.board.boardGraphic[7][4].img == ['♔ ', '♚ ']:
                    if self.CheckToVoid(7, 6) and self.CheckToVoid(7, 5):
                        oponentCanMove = self.GetAllOponentPothitionToAttak()
                        if not (7, 6) in oponentCanMove and not (7, 4) in oponentCanMove:
                            moveFigureIndex = self.findFigure(
                                moveFrom[0], moveFrom[1], self.queue)
                            canMove = CanMove(
                                self.blackFigures[moveFigureIndex].x, self.blackFigures[moveFigureIndex].y, self.board, self.GetAllOponentPothitionToAttak()).canMove
                            if (moveTo[0], moveTo[1]) in canMove:
                                figure = self.blackFigures.pop(moveFigureIndex)
                                figure.x = moveTo[0]
                                figure.y = moveTo[1]
                                self.blackFigures.append(figure)
                                kingIndex = self.findFigure(7, 4, self.queue)
                                king = self.blackFigures.pop(kingIndex)
                                king.x = 7
                                king.y = 6
                                self.blackFigures.append(king)
                                self.queue = 1 if self.queue == 0 else 0
                                self.board.SetFigures(
                                    self.whiteFigures, self.blackFigures)
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
            else:
                return False

    def MoveFigure(self, fromTo):
        moveFrom = (int(fromTo[1])-1, fromTo[0])
        moveFrom = (moveFrom[0], self.ConvertLetterToNumber(moveFrom[1]))
        moveTo = (int(fromTo[-1])-1, fromTo[-2])
        moveTo = (moveTo[0], self.ConvertLetterToNumber(moveTo[1]))

        moveFigureIndex = self.findFigure(moveFrom[0], moveFrom[1], self.queue)
        moveToFigureIndex = self.findFigure(
            moveTo[0], moveTo[1], 1 if self.queue == 0 else 0)
        if moveFigureIndex != None:
            if not self.Castling(moveFrom, moveTo):
                canMove = CanMove(self.whiteFigures[moveFigureIndex].x, self.whiteFigures[moveFigureIndex].y, self.board, self.GetAllOponentPothitionToAttak()).canMove if self.queue == 0 \
                    else CanMove(self.blackFigures[moveFigureIndex].x, self.blackFigures[moveFigureIndex].y, self.board, self.GetAllOponentPothitionToAttak()).canMove
                if (moveTo[0], moveTo[1]) in canMove:
                    figure = self.whiteFigures.pop(
                        moveFigureIndex) if self.queue == 0 else self.blackFigures.pop(moveFigureIndex)
                    if moveToFigureIndex != None:
                        self.blackFigures.pop(
                            moveToFigureIndex) if self.queue == 0 else self.whiteFigures.pop(moveToFigureIndex)
                    figure.x = moveTo[0]
                    figure.y = moveTo[1]
                    self.whiteFigures.append(figure) if self.queue == 0 \
                        else self.blackFigures.append(figure)
                    self.pawnToQuin()
                    self.queue = 1 if self.queue == 0 else 0
                    self.board.SetFigures(self.whiteFigures, self.blackFigures)
                    return True
                else:
                    False
        else:
            return False

    def findFigure(self, x, y, color):
        findIn = self.whiteFigures if color == 0 else self.blackFigures
        for item in findIn:
            if item.x == x and item.y == y:
                return findIn.index(item)

    def ConvertLetterToNumber(self, letter):
        if letter == "a":
            return 0
        elif letter == "b":
            return 1
        elif letter == "c":
            return 2
        elif letter == "d":
            return 3
        elif letter == "e":
            return 4
        elif letter == "f":
            return 5
        elif letter == "g":
            return 6
        elif letter == "h":
            return 7
        else:
            return "Error"


control = Controller()
# board = CanMove.Vizualize(CanMove(0, 0, control.board, control.GetAllOponentPothitionToAttak()))
# print(board)

while True:
    print(control.board)
    control.MoveFigure(input())
