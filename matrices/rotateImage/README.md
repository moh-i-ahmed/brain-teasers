# Rotate Image

[Leetcode link](https://leetcode.com/problems/rotate-image/).

**Description:** You are given an ****nxn* 2D*** matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

#### [Solution](/matrices/rotateImage/solution.py): Extend input matrix by *n* columns then traverse matrix from the bottom up and append each row value and it to a new column.

[Leetcode submission](https://leetcode.com/submissions/detail/1029916726/)

**Explanation:**

1. Extend the matrix to the right by *n* columns, noting where the original matrix ended.
2. Traverse the matrix from the bottom up, copying row values to the newly added column. Essentially turning the rows into columns.
3. After traversing the matrix, remove the original matrix columns.

Time Complexity: **Θ(n<sup>2</sup>)** due to traversing *nxn* matrix
Space Complexity: **Θ(1)**

```python
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # step 1 - extend cols
    for i in range(len(matrix)): matrix.append([])

    # note where original matrix ended
    orgEnd = len(matrix[0])

    # step 2 - traverse matrix from bottom up
    for row in reversed(range(len(matrix[0]))):

        # get position where extended matrix begins
        newCol = len(matrix[0])

        for col in range(len(matrix[0])) :
            # add value to newly created column
            matrix[newCol].append(matrix[row][col])
            newCol += 1

    # step 3 - remove original matrix
    for row in reversed(range(len(matrix[0]))): matrix.pop(row)
```
