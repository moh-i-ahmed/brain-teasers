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

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


def testCases() :
    
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    assert myQueue.peek() == 1
    assert myQueue.pop() == 1
    assert myQueue.empty() == False

    pass

# run tests
testCases()
print("Pass")
