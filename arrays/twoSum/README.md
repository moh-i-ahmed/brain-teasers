# Two Sum

Leetcode link [here](https://leetcode.com/problems/two-sum/).

**Description:** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### [Basic Solution](/arrays/twoSum/solution.py): Compare all values

[Leetcode submission](https://leetcode.com/problems/two-sum/submissions/961965952/)

**Explanation:** Compare each number to all others in the array until target is found.

Time Complexity: **Θ(n)^2**
Space Complexity: **Θ(1)**

```python
"""
:type nums: List[int]
:type target: int
:rtype: List[int]
"""

# base case
if( (len(nums) == 2) and (nums[0] + nums[1] == target) ) :
    return [0, 1]

else :
    # compare each number to everything else in list (O(n)^2)
    for topIndex, num in enumerate(nums) :
        for innerIndex, otherNum in enumerate(nums) :
            # ignore self
            if(topIndex == innerIndex) : continue

            # find target
            if(num + otherNum == target ) : return [ topIndex, innerIndex ]
```
