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

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


def testCases() :
    
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    assert myStack.top() == 2
    assert myStack.pop() == 2
    assert myStack.empty() == False

    pass

# run tests
testCases()
print("Pass")
