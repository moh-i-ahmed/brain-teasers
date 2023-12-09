# Evaluate Reverse Polish Notation

[Leetcode link](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/).

**Description:** You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.


#### [Solution](/stacks&queues/evaluateReversePolishNotation/solution.py): Traverse tokens, add integers to a stack, perform arithmetic of top 2 elements when an operand is found & add the result to the stack.

[Leetcode submission](https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1115931460/)

**Explanation:**

1. Create a set of operands and a stack.
2. Traverse all tokens, doing one of the following:
    - if integer, add to stack.
    - if operand, perform arithmetic of top 2 elements in stack, add result to the stack.
3. After traversing all tokens, only 1 element will remain in the stack, return it.

Time Complexity: **Θ(n)**
Space Complexity: **Θ(n)**

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {'+','-','*','/'}
        stack = []

        for n in tokens:
            # add intgers to stack
            if n not in operands:
                stack.append(int(n))
            # operand found, do math for top 2 integers & add back to stack
            else:
                r = stack.pop()
                l = stack.pop()
                stack.append(int(self.doMath(n, l, r)))

        # stack should only have 1 element, return it
        return stack[0]

    # arithmetic helper function
    def doMath(self, operand, l, r):
        if operand == '+':
            return l + r
        if operand == '-':
            return l - r
        if operand == '*':
            return l * r
        if operand == '/':
            return l / r
```
