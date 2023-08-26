class Solution(object):
    def searchMatrix(matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0])

        if(len(matrix) == 1) :
            if(len(matrix[0]) == 0) : return False
            if(len(matrix[0]) == 1 and matrix[0][0] == target) : return True

        # boundaries of the matrix
        top, bottom = 0, rows-1

        # binary search the column 0 to find range that target is in
        while(top <= bottom) :

            #find mid of column zero
            mid = (top + bottom) // 2

            for row in [ top, bottom, mid ] :
                if(matrix[row][0] == target) : return True

            if(target > matrix[mid][-1]) :
                top = mid + 1

            elif(target < matrix[mid][0]) :
                bottom = mid - 1
            else :
                break

        if( not top <= bottom ) : return False
        targetRow = (top + bottom) // 2

        left, right = 0, len(matrix[0]) -1

        # binary search valid row range for target
        while(left <= right) :
            mid = (left + right) // 2

            if(target > matrix[targetRow][mid]) :
                left = mid + 1
            
            elif(target < matrix[targetRow][mid]) :
                right = mid - 1
    
            elif(matrix[targetRow][mid] == target) :
                return True

        return False


def testCases() :
    testValues = [
        { 'matrix' : [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 'target' : 3,  'answer' : True },
        { 'matrix' : [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 'target' : 11, 'answer' : True },
        { 'matrix' : [[1,3]], 'target' : 2, 'answer' : False },
        { 'matrix' : [[1,3]], 'target' : 1, 'answer' : True },
        { 'matrix' : [[]],    'target' : 1, 'answer' : False },
    ]

    for values in testValues :
        answer = Solution.searchMatrix( matrix=values['matrix'], target=values['target'] )
        print( "Expected %s, got %s" % ( values['answer'], answer ) )
        assert answer == values['answer']

    pass

# run tests
testCases()
print("Pass")
