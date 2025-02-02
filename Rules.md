### A cell's new status is determined by the following rules:

- If the cell's current status is "alive":

  - With fewer than two living neighboring cells, the cell dies (underpopulation).
  - With two or three living neighboring cells, the cell survives.
  - If the cell has more than three living neighboring cells, it dies (overpopulation).

- If the cell is "dead":
  - The cell becomes "alive" (reproduction) if it has exactly three living neighbors.
