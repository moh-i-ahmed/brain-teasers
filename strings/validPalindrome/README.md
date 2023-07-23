# Valid Palindrome

[Leetcode link](https://leetcode.com/problems/valid-palindrome/).

**Description:** A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

#### [Basic Solution](/strings/validPalindrome/solution.py): Clean up string and check the reversed string matches the input string. (Somewhat brute force)

[Leetcode submission](https://leetcode.com/submissions/detail/995071688/)

**Explanation:** Clean up the string by removing white spaces and none alpha-numeric characters. Define a set of valid characters. Compare the input string to the reversed string.

Time Complexity: **Θ(nlog(n))**
Space Complexity: **Θ(1)**

```python
    """
    :type s: str
    :rtype: bool
    """
    # base case, empty string
    if( len(s) <= 1 ) : return True

    alphabet = { 'a','b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'}
    
    # pre-processing, change to lowercase & remove none alphabet chars
    s = s.lower().strip()

    for i in s :
        if( i not in alphabet ) : s = s.replace(i, '')
    
    return s == s[::-1]
```

**Discussion:** The basic solution does not scale well as it's a bit brute force. The pre-processing alone is resource intensive as the replace operation could take **Θ(n)** time.
