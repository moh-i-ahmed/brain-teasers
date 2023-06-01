class Solution():
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # base case
        if( (len(nums) == 2) and (nums[0] + nums[1] == target) ) :
            return [0, 1]

        else :
            # compare each number to everything else in list (O(n)^2)
            for topIndex, num in enumerate(nums) :
                for innerIndex, otherNum in enumerate(nums) :
                    # ignore self
                    if(topIndex == innerIndex) : continue

                    # find target
                    if(num + otherNum == target ) : return [ topIndex, innerIndex ]


def testBaseCases() :
    answer = Solution.twoSum( nums=[ 1, 2 ], target=3 )
    print( "Expected %s, solution %s" % ( [ 0, 1 ], answer ) )
    assert answer == [ 0, 1 ]

    pass

def testRegularCases() :
    answer = Solution.twoSum( nums=[ 2, 7, 4, 5 ], target=12 )
    print( "Expected %s, solution %s" % ( [ 1, 3 ], answer ) )
    assert answer == [ 1, 3 ]

    pass

# run tests
testBaseCases()
testRegularCases()
