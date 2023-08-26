# Search a 2D Matrix

[Leetcode link](https://leetcode.com/problems/search-a-2d-matrix/).

**Description:** You are given an m x n integer matrix matrix with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

#### [Basic Solution](/searching/search2DMatrix/solution.py): Binary search the first column to find the 'target row' to inspect (search space), then binary search the target row. 

[Leetcode submission](https://leetcode.com/submissions/detail/1032464835/)

**Explanation:**

1. Initialize variables to track the top and bottom pointers of the matrix.
2. Since the matrix is sorted, we can binary search the first column using the top and bottom pointers to find the search space i.e. the row that may contain the target.
3. We then binary search the row (left to right pointers) to find the target.
4. If target is found, return *True*, otherwise *False*.

Time Complexity: **Θ(log(m * n))**
Space Complexity: **Θ(1)**

```python
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    rows, cols = len(matrix), len(matrix[0])

    # weird edge case
    if(len(matrix) == 1) :
        if(len(matrix[0]) == 0) : return False
        if(len(matrix[0]) == 1 and matrix[0][0] == target) : return True

    # boundaries of the matrix
    top, bottom = 0, rows-1

    # binary search the column 0 to find range that target is in
    while(top <= bottom) :

        #find mid of column zero
        mid = (top + bottom) // 2

        for row in [ top, bottom, mid ] :
            if(matrix[row][0] == target) : return True

        if(target > matrix[mid][-1]) :
            top = mid + 1

        elif(target < matrix[mid][0]) :
            bottom = mid - 1
        else :
            break

    if( not top <= bottom ) : return False
    targetRow = (top + bottom) // 2

    left, right = 0, len(matrix[0]) -1

    # binary search valid row range for target
    while(left <= right) :
        mid = (left + right) // 2

        if(target > matrix[targetRow][mid]) :
            left = mid + 1
        
        elif(target < matrix[targetRow][mid]) :
            right = mid - 1

        elif(matrix[targetRow][mid] == target) :
            return True

    return False
```
