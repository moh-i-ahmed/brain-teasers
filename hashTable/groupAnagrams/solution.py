from random import randint

class Solution(object):
    def groupAnagrams(strs):
        
        # base cases
        if len(strs) < 2: return [] if len(strs) == 0 else [strs]
                
        unique = {}

        for s in strs:
            uniq = str(sorted(s))

            if uniq not in unique:
                unique[uniq] = [s]
            else:
                unique[uniq].append(s)
            
        return list(unique.values())


def testCases() :
    testValues = [
        { 'strs' : ["eat","tea","tan","ate","nat","bat"], 'answer' : [["eat","tea","ate"],["tan","nat"],["bat"]] },
        { 'strs' : ["a"], 'answer' : [["a"]] },
        { 'strs' : [""],  'answer' : [[""]] },
    ]

    for values in testValues :
        answer = Solution.groupAnagrams( strs=values['strs'] )
        print( "Expected %s, got %s" % ( values['answer'], answer ) )
        assert answer == values['answer']

    pass

# run tests
testCases()
print("Pass")