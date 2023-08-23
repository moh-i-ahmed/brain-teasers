class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # step 1 - extend cols
        for i in range(len(matrix)): matrix.append([])

        # note where original matrix ended
        orgEnd = len(matrix[0])

        # step 2 - traverse matrix from bottom up
        for row in reversed(range(len(matrix[0]))):

            # get position where extended matrix begins
            newCol = len(matrix[0])


            for col in range(len(matrix[0])) :

                # add value to newly created column
                matrix[newCol].append(matrix[row][col])
                newCol += 1

        # step 3 - remove original matrix
        for row in reversed(range(len(matrix[0]))): matrix.pop(row)

        return matrix


def testCases() :
    testValues = [
        { 'matrix' : [[1,2,3],[4,5,6],[7,8,9]],                        'answer' : [[7,4,1],[8,5,2],[9,6,3]] },
        { 'matrix' : [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], 'answer' : [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]] },
    ]

    for values in testValues :
        answer = Solution.setZeroes( values['matrix'] )
        print( "Expected %s, got %s" % ( values['answer'], answer ) )
        assert answer == values['answer']

    pass

# run tests
testCases()
print("Pass")
