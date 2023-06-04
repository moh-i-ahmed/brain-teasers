# Contains Duplicate

[Leetcode link](https://leetcode.com/problems/contains-duplicate/)

**Description:** Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#### [Basic Solution](/arrays/containsDuplicate/solution.py): Mark seen items in a hash table.

[Leetcode submission](https://leetcode.com/problems/contains-duplicate/submissions/963682604/)

**Explanation:** Iterate through the list, marking seen items in a dictionary. Return ___True___ once we find an item that's already been marked in the dictionary (duplicate). Otherwise, return ___False___.

Time Complexity: **Θ(n)**
Space Complexity: **Θ(1)**

```python
    """
    :type nums: List[int]
    :rtype: bool
    """
    seen = {}

    for n in nums :
        if(n not in seen) :
            seen[n] = True
        else :
            return True

    return False
```
