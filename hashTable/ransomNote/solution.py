from random import randint

class Solution(object):
    def canConstruct(ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        # step 1: pre-processing
        ransomLetters, magazineLetters = {}, {}
        
        for i in ransomNote :
            if(i not in ransomLetters) :
                ransomLetters[i] = 1
            else :
                ransomLetters[i] += 1
                
        for i in magazine :
            if(i not in magazineLetters) :
                magazineLetters[i] = 1
            else :
                magazineLetters[i] += 1
        
        canConst = None

        # step 2: check if magazine has enough of each letter in ransomNote
        for l, count in ransomLetters.items():
            if(l not in magazineLetters) :
                return False
            else :
                if(magazineLetters[l] >= count ) :
                    canConst = True
                else :
                    return False
        
        return canConst


def testRegularCases() :
    testValues = [
        { 'ransomNote' : "a", 'magazine' : "b", 'answer' : False },
        { 'ransomNote' : "aa", 'magazine' : "ab", 'answer' : False },
        { 'ransomNote' : "aa", 'magazine' : "aab", 'answer' : True },
    ]

    for values in testValues :
        answer = Solution.canConstruct( ransomNote=values['ransomNote'], magazine=values['magazine'] )
        print( "Expected %s, got %s" % ( values['answer'], answer ) )
        assert answer == values['answer']

    pass

# run tests
testRegularCases()
print("Pass")
