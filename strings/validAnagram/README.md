# Valid Anagram

[Leetcode link](https://leetcode.com/problems/valid-anagram/).

**Description:** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#### [Basic Solution](/strings/validAnagram/solution.py): Sorted input strings, expect they're the same.

[Leetcode submission](https://leetcode.com/submissions/detail/995006902/)

**Explanation:** Check the sorted input strings are the same. Time complexity goes up due to the string sort operations.

Time Complexity: **Θ(nslog(n))** - where s is the length of the string
Space Complexity: **Θ(1)**

```python
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    return sorted(s) == sorted(t)
```
