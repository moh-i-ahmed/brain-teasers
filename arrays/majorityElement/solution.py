class Solution(object):
    def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # dict counting seen elements
        seen = {}
        
        # count occurrences of each element
        for i in nums :
            if( i not in seen ) :
                seen[i] = 1
            else :
                seen[i] += 1
        
        # track majority element and num occurrences
        majElement, majCount = -1, -1

        # get the highest occurring element
        for element, count in seen.items() :
            if( count > majCount ) :
                majElement = element
                majCount = count
        
        return majElement


def testRegularCases() :
    testValues = [ 
        { 'nums' : [ 3, 2, 3 ], 'answer' : 3 },
        { 'nums' : [ 2, 2, 1, 1, 1, 2, 2 ], 'answer' : 2 },
        { 'nums' : [ 1, 2, 3, 4, 1 ], 'answer' : 1 },
    ]

    for values in ( testValues ) :
        answer = Solution.majorityElement( nums=values['nums'] )
        print( "Expected %s, solution %s" % ( values['nums'], answer ) )
        assert answer == values['answer']

    pass

# run tests
testRegularCases()
print("Pass")
