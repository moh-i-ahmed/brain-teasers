# Group Anagrams

[Leetcode link](https://leetcode.com/problems/group-anagrams/).

**Description:** Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#### [Solution](/strings/groupAnagrams/solution.py): Store each word in a list (hashmap value), using the sorted string as the key.

**Explanation:** Create a hash table then iterate through input list of strings:

1. Sort each string then check if the sorted string is present as a key in the hash table:
    - if key is not present, add key to hash table and set its value to a list containing the unsorted string.
    - if key is present, add unsorted string to the list of values.
2. Return list of hash table values.

Time Complexity: **Θ(nlog(n))**
Space Complexity: **Θ(n)** - worst case

[Leetcode submission 1](https://leetcode.com/submissions/detail/1034264951/)
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

[Leetcode submission 2](https://leetcode.com/submissions/detail/1097363902/)
```python
    # base cases
    if len(strs) < 2: return [] if len(strs) == 0 else [strs]

    unique = {}
    for s in strs:
        uniq = str(sorted(s))

        if uniq not in unique:
            unique[uniq] = [s]
        else:
            unique[uniq].append(s)

    return unique.values()
```
