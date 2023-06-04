from random import randint

class Solution():
    def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # base cases
        if(not nums) :
            return 0
        if(len(nums) == 1) :
            return nums[0]

        sum = maxSum = nums[0]

        for n in nums[1:] :
            sum = n if(n > sum+n) else sum + n
            maxSum = sum if(sum > maxSum) else maxSum

        return maxSum


def testBaseCases() :
    answer = Solution.maxSubArray( nums=[] )
    print( "Expected %s, got %s" % ( 0, answer ) )
    assert answer == 0

    num = randint(0,100)
    answer = Solution.maxSubArray( nums=[num] )
    print( "Expected %s, got %s" % ( num, answer ) )
    assert answer == num

    pass

def testRegularCases() :
    testValues = [
        { 'nums' : [-2,1,-3,4,-1,2,1,-5,4], 'answer' : 6 },
        { 'nums' : [5,4,-1,7,8], 'answer' : 23 },
        { 'nums' : [-2,-1], 'answer' : -1 },
    ]

    for values in testValues :
        answer = Solution.maxSubArray( nums=values['nums'] )
        print( "Expected %s, got %s" % ( values['answer'], answer ) )
        assert answer == values['answer']

    pass

# run tests
testBaseCases()
testRegularCases()
print("Pass")
