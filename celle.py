class Celle:
    def __init__(self):
        self._alive = False
        self._neighbours = []
        self._livingNeighbours = 0

    
    def setAlive(self):
        self._alive = True
    
    def setDead(self):
        self._alive = False

    def isAlive(self):
        return self._alive
    
    def getStatus(self):
        return "O" if self.isAlive() else "-"
    
    def addNeighbour(self, neighbour):
        self._neighbours.append(neighbour)
    
    def countLivingNeighbours(self):
        return sum(1 for n in self._neighbours if n._alive)
    
    def updateStatus(self):
        # Rule nr. 4
        if not self.isAlive():
            if self.countLivingNeighbours() == 3:
                self.setAlive()
                return
            return
        
        # Rule nr. 1 and 3
        livingNeighbours = self.countLivingNeighbours()
        if (livingNeighbours > 3 or livingNeighbours < 2):
            self.setDead()
            return
        
        # Rule nr. 2 -> None of above and cell lives on
        




            


def Test():
    c = Celle()

    n = Celle()

    x = Celle()

    x.setAlive()

    c.addNeighbour(n)
    c.addNeighbour(x)

    print(c.countLivingNeighbours())



