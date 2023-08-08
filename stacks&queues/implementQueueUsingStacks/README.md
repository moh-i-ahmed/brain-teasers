# Implement Queue using Stacks

[Leetcode link](https://leetcode.com/problems/implement-queue-using-stacks/).

**Description:** Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

*void push(int x)* - Pushes element x to the back of the queue.
*int pop()* - Removes the element from the front of the queue and returns it.
*int peek()* - Returns the element at the front of the queue.
*boolean empty()* - Returns true if the queue is empty, false otherwise.

#### [Basic Solution](/stacks&queues/implementQueueUsingStacks/solution.py): Use a list as the base data structure.

[Leetcode submission](https://leetcode.com/submissions/detail/1015541988/)

Time complexity of methods: **Θ(1)**

```python
class MyQueue(object):

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
        if(len(self.data) > 0) :
            removed = self.data[0]
            self.data = self.data[1:]

        return removed
        

    def peek(self):
        """
        :rtype: int
        """
        head = None
        if(len(self.data) > 0) : head = self.data[0]
        return head

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.data) == 0
```
