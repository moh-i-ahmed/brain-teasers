class Solution():
    def isValid(s: str) -> bool:
        
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
            
        # dangling open bracket
        if openB: return False

        return True


def testCases() :
    testValues = [
        { 's' : "()",     'answer' : True },
        { 's' : "(]",     'answer' : False },
        { 's' : "(){}}{", 'answer' : False },
        { 's' : "((",     'answer' : False },
        { 's' : "()[]{}", 'answer' : True },
    ]

    for values in testValues :
        answer = Solution.isValid( s=values['s'] )
        print( "Expected %s, got %s" % ( values['answer'], answer ) )
        assert answer == values['answer']

    pass

# run tests
testCases()
print("Pass")
