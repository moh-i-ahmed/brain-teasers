# Majority Element

Leetcode link [here](https://leetcode.com/problems/majority-element/).

**Description:** Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

### [Basic Solution](/arrays/majorityElement/solution.py): Count the occurrences of each element and take the max.

[Leetcode submission](https://leetcode.com/submissions/detail/1000920363/)

**Explanation:** Iterate through the list and count the occurrences of the elements in a dictionary. Go through the dictionary and pick the select the most occurring element.

Time Complexity: **Θ(n)**
Space Complexity: **Θ(n)**

```python
"""
    :type nums: List[int]
    :rtype: int
    """
    # dict counting seen elements
    seen = {}
    
    # count occurrences of each element
    for i in nums :
        if( i not in seen ) :
            seen[i] = 1
        else :
            seen[i] += 1
    
    # track majority element and num occurrences
    majElement, majCount = -1, -1

    # get the highest occurring element
    for element, count in seen.items() :
        if( count > majCount ) :
            majElement = element
            majCount = count
    
    return majElement
```
