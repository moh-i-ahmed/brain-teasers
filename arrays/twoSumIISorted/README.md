# Two Sum II - Input Array Is Sorted

Leetcode link [here](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/).

**Description:** Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

### [Basic Solution](/arrays/twoSumIISorted/solution.py): Two-pointer method

[Leetcode submission](https://leetcode.com/submissions/detail/1096867285/)

**Explanation:** Use a pointer at either end and move inward until the target sum is found or the pionters meet (target sum not found).

Time Complexity: **Θ(n)**
Space Complexity: **Θ(1)**

```python
"""
:type nums: List[int]
:type target: int
:rtype: List[int]
"""
l, r = 0, len(numbers) - 1

while l < r:
    lVal = numbers[l]
    rVal = numbers[r]
    
    if lVal + rVal == target:
        return [l+1, r+1]
    else:
                        
        if lVal + rVal < target:
            l += 1
        elif lVal + rVal > target:
            r -= 1
            
return [ l+1, r+1 ]
```
