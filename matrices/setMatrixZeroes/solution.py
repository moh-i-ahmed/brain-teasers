class Solution(object):
    def setZeroes(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        affectedRows, affectedCols = set(), set()
        
        # step 1: iterate through matrix and mark rows/columns with zeroes
        for rowInd, r in enumerate(matrix) :
            for colInd, c in enumerate(matrix[rowInd]) :
                if(matrix[rowInd][colInd] == 0) :
                    affectedRows.add(rowInd)
                    affectedCols.add(colInd)
                    
        # step 2a - set all values in row to zero if any zero was found
        for r in list(affectedRows) :
            for index, val in enumerate(matrix[r]) :
                matrix[r][index] = 0
                
        # step2b - set all values in columns to zero if any zero was found
        for rowInd, r in enumerate(matrix) :
            for c in list(affectedCols) :
                matrix[rowInd][c] = 0

        return matrix


def testCases() :
    testValues = [
        { 'matrix' : [[1,1,1],[1,0,1],[1,1,1]],       'answer' : [[1,0,1],[0,0,0],[1,0,1]] },
        { 'matrix' : [[0,1,2,0],[3,4,5,2],[1,3,1,5]], 'answer' : [[0,0,0,0],[0,4,5,0],[0,3,1,0]] },
    ]

    for values in testValues :
        answer = Solution.setZeroes( values['matrix'] )
        print( "Expected %s, got %s" % ( values['answer'], answer ) )
        assert answer == values['answer']

    pass

# run tests
testCases()
print("Pass")
