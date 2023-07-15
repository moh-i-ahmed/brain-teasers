from random import randint

class Solution(object):
    def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        # base case
        if( 0 <= len(s) <= 1 ) : return True

        alphabet = { 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'}
        
        # pre-processing, change to lowercase & remove not alphabet chars
        s = s.lower().strip()

        for i in s :
            if( i not in alphabet ) : s = s.replace(i, '')

        return s == s[::-1]


def testRegularCases() :
    testValues = [
        { 's' : "", 'answer' : True },
        { 's' : "z", 'answer' : True },
        { 's' : "0P", 'answer' : False },
        { 's' : "1234321", 'answer' : True },
        { 's' : "A man, a plan, a canal: Panama", 'answer' : True },
    ]

    for values in testValues :
        answer = Solution.isPalindrome( s=values['s'] )
        print( "Expected %s, got %s" % ( values['answer'], answer ) )
        assert answer == values['answer']

    pass

# run tests
testRegularCases()
print("Pass")
