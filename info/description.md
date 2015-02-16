The durability map is represented as a matrix with digits. Each number is the durability measurement for the cell.
To find the weakest point we should find the weakest row and column. 
The weakest point is placed in the intersection of these rows and columns. 
Row (column) durability is a sum of cell durability in that row (column). 
You should find coordinates of the weakest point (row and column). 
The first row (column) is 0th row (column). If a section has several equal weak points, then choose the top left point.

![Weak Point](weak-point.svg)
