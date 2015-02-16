For a sniper it's very important to find a weak point in a target.

The durability map is represented as a matrix with digits. Each number is the durability measurement for the cell.
To find the weakest point we should find the weakest row and column. 
The weakest point is placed in the intersection of these rows and columns. 
Row (column) durability is a sum of cell durability in that row (column). 
You should find coordinates of the weakest point (row and column). 
The first row (column) is 0th row (column). If a section has several equal weak points, then choose the top left point.

![Weak Point](weak-point.svg)

**Input:** A durability map as a list of lists with integers. 

**Output:** The coordinates of the weak point as a list (tuple) of integers.
 
**Example:**

```python
weak_point([[7, 2, 7, 2, 8],
        [2, 9, 4, 1, 7],
        [3, 8, 6, 2, 4],
        [2, 5, 2, 9, 1],
        [6, 6, 5, 4, 5]]) == [3, 3]
weak_point([[7, 2, 4, 2, 8],
        [2, 8, 1, 1, 7],
        [3, 8, 6, 2, 4],
        [2, 5, 2, 9, 1],
        [6, 6, 5, 4, 5]]) == [1, 2]
```
**How it is used:**

Matrices (2D array) are an often used data structure and it will be helpful to sharpen your skills with them.

**Precondition:**
```python
0 < len(matrix) <= 10
all(len(row) == len(matrix) for row in matrix)
all(all(0 < x < 10 for x in row) for row in matrix)
```
