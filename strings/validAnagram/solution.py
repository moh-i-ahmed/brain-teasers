from random import randint

class Solution():
    def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return sorted(s) == sorted(t)


def testRegularCases() :
    testValues = [
        { 's' : "anagram", 't' : "nagaram", 'answer' : True },
        { 's' : "anagram", 't' : "naram",   'answer' : False },
        { 's' : "margana", 't' : "anagram", 'answer' : True },
    ]

    for values in testValues :
        answer = Solution.isAnagram( s=values['s'], t=values['t'] )
        print( "Expected %s, got %s" % ( values['answer'], answer ) )
        assert answer == values['answer']

    pass

# run tests
testRegularCases()
print("Pass")
