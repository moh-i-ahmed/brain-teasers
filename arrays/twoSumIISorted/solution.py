class Solution():
    def twoSum(numbers, target):
        l, r = 0, len(numbers)-1

        while l < r:
            lVal = numbers[l]
            rVal = numbers[r]
            
            if lVal + rVal == target:
                return [l+1,r+1]
            else:
                                
                if lVal + rVal < target:
                    l += 1
                elif lVal + rVal > target:
                    r -= 1
                    
        return [l+1,r+1]



def testCases() :
    testValues = [ 
        { 'nums' : [ 2, 7, 11, 15 ],   'target' : 9,  'indices' : [ 1, 2 ] },
        { 'nums' : [ 2, 3, 4 ],        'target' : 6,  'indices' : [ 1, 3 ] },
        { 'nums' : [ 1, 3, 5, 9, 12 ], 'target' : 14, 'indices' : [ 3, 4 ] },
    ]

    for values in ( testValues ) :
        answer = Solution.twoSum( numbers=values['nums'], target=values['target'] )
        print( "Expected %s, got %s" % ( values['indices'], answer ) )
        assert answer == values['indices']

    pass

# run tests
testCases()
print("Pass")
