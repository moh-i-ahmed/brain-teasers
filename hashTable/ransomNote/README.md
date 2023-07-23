# Ransome Note

[Leetcode link](https://leetcode.com/problems/ransom-note/).

**Description:** Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

#### [Basic Solution](/hashTable/ransomNote/solution.py): Count the occurrences of each letter in both input strings then check if there are enough letters to build *ransomNote*.

[Leetcode submission](https://leetcode.com/submissions/detail/1002132933/)

**Explanation:** Check if there are enough ingredients (magazine) to build the recipe (ransomNote).
Count the occurrences of each letter in both input strings; ransomNote (recipe) and magazine (ingredients) in hash tables then check if there are enough ingredients to build the recipe.

1. Pre-process the input strings by counting the occurrences of each letter into hash tables.
2. Define variable to store answer
3. For each letter in the *ransomNote* hash table, check if the *magazine* hash table has enough occurrences of the same letter.
4. When there are fewer occurrences of a letter or a letter is missing in the *magazine* hash table, return *False*.

Time Complexity: **Θ(n)**
Space Complexity: **Θ(2n) == Θ(n)**

```python
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
 
    # step 1: pre-processing
    ransomLetters, magazineLetters = {}, {}
    
    for i in ransomNote :
        if(i not in ransomLetters) :
            ransomLetters[i] = 1
        else :
            ransomLetters[i] += 1
            
    for i in magazine :
        if(i not in magazineLetters) :
            magazineLetters[i] = 1
        else :
            magazineLetters[i] += 1
    
    canConst = None

    # step 2: check each letter in ransomNote is available in magazine
    for l, count in ransomLetters.items():
        if(l not in magazineLetters) :
            return False
        else :
            if(magazineLetters[l] >= count ) :
                canConst = True
            else :
                return False
    
    return canConst
```
