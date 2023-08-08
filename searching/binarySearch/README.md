# Binary Search

[Leetcode link](https://leetcode.com/problems/binary-search/).

**Description:** Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

#### [Basic Solution](/searching/binarySearch/solution.py): Continuously split the input array in two, target is either the middle, on the left or right of the middle, or not in the array. (Sliding Window) 

[Leetcode submission](https://leetcode.com/submissions/detail/1015531930/)

**Explanation:** Find the middle point of the array, since the array is sorted the target has to be:

1. the middle
2. to the left of the middle, reduce the right pointer to middle-1 index
3. to the right of the middle, increase the left pointer to middle+1 index
4. repeat steps above until array size is one, at that point, it's either the target or not in the array.

Time Complexity: **Θ(log(n))**
Space Complexity: **Θ(1)**

```python
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if(len(nums) == 0) : return -1
    if(len(nums) == 1) :
        return 0 if(nums[0] == target) else -1
    
    left = 0
    right = len(nums) - 1
    
    while left <= right :
        mid = (left+right) // 2
            
        if(nums[mid] == target) :
            return mid
        else :
            if(nums[mid] > target):
                right = mid - 1
            elif(nums[mid] < target):
                left = mid + 1
    
    return -1
```
