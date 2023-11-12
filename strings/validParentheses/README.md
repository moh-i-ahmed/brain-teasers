# Valid Parentheses

[Leetcode link](https://leetcode.com/problems/valid-parentheses/).

**Description:** Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

#### [Basic Solution](/strings/validParantheses/solution.py): Use a stack to track open brackets and expect closing brackets to match the top of the stack.

[Leetcode submission](https://leetcode.com/submissions/detail/1097329369/)

**Explanation:** Iterate through string and add any open bracket (OB) to a stack. When a closing bracket (CB) is encountered, check that it matches the opening bracket at the top of the stack, otherwise return False. After iterating throught the string, if the stack is empty then all brackets have been matched - return True, otherwise a dangling open bracket exists - return False.

Time Complexity: **Θ(n)**

```python
    openB = []
    pairs = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
    }
    
    # base case || corner case
    if (len(s) < 2) or (s[0] in pairs.keys()) : return False
    
    for c in s:

        # add open bracket to stack
        if c in pairs.values():
            openB.append(c)
        
        # look for matching open bracket at top of stack
        elif c in pairs.keys():
            if openB and openB[-1] == pairs[c]:
                openB.pop()
            else:
                return False
        else:
            return False
        
    # dangling open bracket exists
    if openB: return False
    
    return True
```
