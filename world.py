from grid import Grid


class World:
    def __init__(self, rows, cols):
        self._grid = Grid(rows, cols)
        self._generations = 0
        self._grid.fillGrid()
        self._grid.connectCells()
    
    def draw(self):
        self._grid.drawGrid()
        print(f"Num generations: {self._generations}\n")
        print(f"Living cells: {self._grid.countLiving()}\n")

    
    def update(self):
        for cell in self._grid.getAllCells():
            cell.countLivingNeighbours()
            cell.updateStatus()
        self._generations += 1
    
    


        