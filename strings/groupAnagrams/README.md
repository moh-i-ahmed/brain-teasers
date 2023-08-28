# Group Anagrams

[Leetcode link](https://leetcode.com/problems/group-anagrams/).

**Description:** Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#### [Basic Solution](/strings/groupAnagrams/solution.py): Store each word in a list (hashmap value), using the sorted string as the key.

[Leetcode submission](https://leetcode.com/submissions/detail/1034264951/)

**Explanation:** Sort each string and add to hashmap (dictionary). Store each unsorted string in a list (value) with the sorted string as the key.

Time Complexity: **Θ(nlog(n))**
Space Complexity: **Θ(n)**

```python
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    if(len(strs) == 0)  : return strs
    
    anagrams = {}
    
    for word in strs:
        sortedWord = str(sorted(word))
        if(sortedWord not in anagrams):
            anagrams[sortedWord] = []
        
        anagrams[sortedWord].append(word)
        
    return list(anagrams.values())
```
