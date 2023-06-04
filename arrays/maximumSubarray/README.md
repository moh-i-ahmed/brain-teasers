# Maximum Subarray

[Leetcode link](https://leetcode.com/problems/maximum-subarray/description/).

**Description:** Given an integer array nums, find the subarray with the largest sum, and return its sum.

#### [Basic Solution](/arrays/maximumSubarray/solution.py): Iterate through array and pick max sum we go.

[Leetcode submission](https://leetcode.com/problems/maximum-subarray/submissions/963664801/)

**Explanation:** Iterate through the list, finding the max sum as we go.

Time Complexity: **Θ(n)**
Space Complexity: **Θ(1)**

```python
    """
    :type nums: List[int]
    :rtype: int
    """

    # base cases
    if(not nums) :
        return 0
    if(len(nums) == 1) :
        return nums[0]

    sum = maxSum = nums[0]

    for n in nums[1:] :
        sum = n if(n > sum+n) else sum + n
        maxSum = sum if(sum > maxSum) else maxSum

    return maxSum
```
