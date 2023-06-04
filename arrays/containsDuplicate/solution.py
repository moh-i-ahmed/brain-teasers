class Solution():
    def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}

        for n in nums :
            if (n not in seen) :
                seen[n] = True
            else :
                return True

        return False


def testRegularCases() :
    testValues = [
        { 'nums' : [1,2,3,1], 'answer' : True },
        { 'nums' : [1,2,3,4], 'answer' : False },
        { 'nums' : [], 'answer' : False },
    ]

    for values in testValues :
        answer = Solution.containsDuplicate( nums=values['nums'] )
        print( "Expected %s, got %s" % ( values['answer'], answer ) )
        assert answer is values['answer']

    pass

# run tests
testRegularCases()
print("Pass")
