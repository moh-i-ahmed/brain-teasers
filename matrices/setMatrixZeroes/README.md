# Set Matrix Zeroes

[Leetcode link](https://leetcode.com/problems/set-matrix-zeroes/).

**Description:** Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

#### [Basic Solution](/searching/setMatrixZeroes/solution.py): Traverse matrix and store rows/columns with zeroes then visit each row and column found and change their values to zeroes (in-place). 

[Leetcode submission](https://leetcode.com/submissions/detail/1028934697/)

**Explanation:**

1. Traverse matrix and mark the row and column of each zero in sets (for uniqueness) to track each respectively, and to avoid having to traverse the entire matrix again.
2. Visit each marked row and set its values to zero.
3. Visit each marked column and set its values to zero.

Time Complexity: **Θ(mn)** as we have to visit each cell in the matrix.
Space Complexity: **Θ(m + n)** due to only needing space for the number of rows & columns that exist.

```python
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    affectedRows, affectedCols = set(), set()
    
    # step 1: iterate through matrix and mark rows/columns with zeroes
    for rowInd, r in enumerate(matrix) :
        for colInd, c in enumerate(matrix[rowInd]) :
            if(matrix[rowInd][colInd] == 0) :
                affectedRows.add(rowInd)
                affectedCols.add(colInd)
                
    # step 2a - set all values in row to zero if any zero was found
    for r in list(affectedRows) :
        for index, val in enumerate(matrix[r]) :
            matrix[r][index] = 0
            
    # step2b - set all values in columns to zero if any zero was found
    for rowInd, r in enumerate(matrix) :
        for c in list(affectedCols) :
            matrix[rowInd][c] = 0
```
