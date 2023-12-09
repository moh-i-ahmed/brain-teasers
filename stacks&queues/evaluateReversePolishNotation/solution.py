class Solution(object):
    def evalRPN(tokens) -> int:
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
                stack.append(int(Solution.doMath(n, l, r)))

        # stack should only have 1 element, return it
        return stack[0]

    # arithmetic helper function
    def doMath(operand, l, r):
        if operand == '+':
            return l + r
        if operand == '-':
            return l - r
        if operand == '*':
            return l * r
        if operand == '/':
            return l / r


def testCases():
    testValues = [
        { 'tokens' : ["2","1","+","3","*"], 'answer' : 9 },
        { 'tokens' : ["4","13","5","/","+"], 'answer' : 6 },
        { 'tokens' : ["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 'answer' : 22 },
    ]

    for values in testValues :
        answer = Solution.evalRPN( tokens=values['tokens'] )
        print( "Expected %s, got %s" % ( values['answer'], answer ) )
        assert answer == values['answer']

    pass

# run tests
testCases()
print("Pass")