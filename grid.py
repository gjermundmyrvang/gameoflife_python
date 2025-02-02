from random import randint

from celle import Celle

class Grid:
    def __init__(self, rows, cols):
        self._numRows = rows
        self._numCols = cols
        self._grid = self.createGrid()
        self.fillGrid()
    
    def createRow(self):
        return [None] * self._numRows
    
    def createGrid(self):
        return [self.createRow() for _ in range(self._numCols)]
    
    def fillGrid(self):
        for i in range(self._numCols):
            for j in range(self._numRows):
                c = Celle()
                self._grid[i][j] = c
                if randint(0, 2) == 0:
                    self._grid[i][j].setAlive()
    
    def getCell(self, x, y):
        if x >= self._numRows or x < 0 or y >= self._numCols or y < 0:
            return None
        
        return self._grid[x][y]
    
    def drawGrid(self):
        print("\n" * 5)
        for row in self._grid:
            print(" ".join(cell.getStatus() for cell in row) )
        print("\n" * 5)
    
    def setNeighbours(self, x, y):
        c = self.getCell(x, y)
        if c is None:
            return
        
        neighbours = [
            self.getCell(x-1, y-1),  # Top left
            self.getCell(x, y-1),    # Top
            self.getCell(x+1, y-1),  # Top right
            self.getCell(x-1, y),    # Left
            self.getCell(x+1, y),    # Right
            self.getCell(x-1, y+1),  # Bottom left
            self.getCell(x, y+1),    # Bottom
            self.getCell(x+1, y+1)   # Bottom right
        ]

        for i in neighbours:
            if i is not None:
                c.addNeighbour(i)
    
    def connectCells(self):
        for i in range(len(self._grid)):
            for j in range(len(self._grid[i])):
                self.setNeighbours(i, j)
    
    def getAllCells(self):
        return [cell for row in self._grid for cell in row]

    def countLiving(self):
        return sum(1 for cell in self.getAllCells() if cell.isAlive())
    



        

    

                

def test():
    g = Grid(10, 10)
    g.connectCells()
    print(g.countLiving())

test()

    




