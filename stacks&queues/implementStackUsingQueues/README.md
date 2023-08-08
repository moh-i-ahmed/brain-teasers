# Implement Stack using Queues

[Leetcode link](https://leetcode.com/problems/implement-stack-using-queues/).

**Description:** Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

*void push(int x)* - Pushes element x to the top of the stack.
*int pop()* - Removes the element on the top of the stack and returns it.
*int top()* - Returns the element on the top of the stack.
*boolean empty()* - Returns true if the stack is empty, false otherwise.

#### [Basic Solution](/stacks&queues/implementStackUsingQueues/solution.py): Use a list as the base data structure.

[Leetcode submission](https://leetcode.com/submissions/detail/1015551622/)

Time complexity of methods: **Θ(1)**

```python
class MyStack(object):

    def __init__(self):
        self.data = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        removed = None
        if(len(self.data) > 0):
            removed = self.data[len(self.data)-1]
            self.data = self.data[:len(self.data)-1]
        
        return removed
        

    def top(self):
        """
        :rtype: int
        """
        return self.data[len(self.data)-1] if(len(self.data) > 0) else None
        

    def empty(self):
        """
        :rtype: bool
        """
        return True if(len(self.data) == 0) else False

```
