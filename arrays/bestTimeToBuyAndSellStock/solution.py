from random import randint

class Solution():
    def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0

        # base case
        if(len(prices) == 0) : return maxProfit

        lowestPrice = float('inf')

        for price in prices :
            # find lowest price
            if(price < lowestPrice) : lowestPrice = price

            # find max profit
            if(price - lowestPrice > maxProfit) : maxProfit = price - lowestPrice

        return maxProfit


def testBaseCases() :
    answer = Solution.maxProfit( prices=[] )
    print( "Expected %s, got %s" % ( 0, answer ) )
    assert answer == 0

    pass

def testRegularCases() :
    testValues = [
        { 'prices' : [7,1,5,3,6,4], 'answer' : 5 },
        { 'prices' : [7,6,4,1,3], 'answer' : 2 },
    ]

    for values in testValues :
        answer = Solution.maxProfit( prices=values['prices'] )
        print( "Expected %s, got %s" % ( values['answer'], answer ) )
        assert answer == values['answer']

    pass

def testRandomCases() :
    testValues = [
        { 'prices' : list(reversed(range(0,100,(randint(1,3))))) + [104], 'answer' : 104 },
    ]

    for values in testValues :
        answer = Solution.maxProfit( prices=values['prices'] )
        print( "Expected %s, got %s" % ( values['answer'], answer ) )
        assert answer == values['answer']

    pass

# run tests
testBaseCases()
testRegularCases()
testRandomCases()
print("Pass")
