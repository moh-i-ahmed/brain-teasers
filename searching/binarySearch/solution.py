from random import randint

class Solution(object):
    def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        ans = -1

        # base cases
        if( len(nums) == 1 ) : return 0 if( nums[0] == target) else ans        
        if( (target < nums[0]) or (target > nums[len(nums)-1]) )  : return ans

        
        left, right = 0, len(nums) - 1
        
        while(left <= right) :

            mid = (left+right) // 2

            if( target == nums[mid] ) :
                return mid

            elif( target > nums[mid] ) :
                left = mid + 1
            else :
                right = mid - 1

        return -1


def testCases() :
    testValues = [
        { 'target' : 9, 'nums' : [-1,0,3,5,9,12], 'answer' : 4 },
        { 'target' : 2, 'nums' : [-1,0,3,5,9,12], 'answer' : -1 },
        { 'target' : 2, 'nums' : [1], 'answer' : -1 },
        { 'target' : 1, 'nums' : [1], 'answer' : 0 },
    ]

    for values in testValues :
        answer = Solution.search( nums=values['nums'], target=values['target'] )
        print( "Expected %s, got %s" % ( values['answer'], answer ) )
        assert answer == values['answer']

    pass

# run tests
testCases()
print("Pass")
