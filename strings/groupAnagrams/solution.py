class Solution(object):
    def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if(len(strs) == 0)  : return strs
        
        anagrams = {}
        
        for word in strs:
            sortedWord = str(sorted(word))
            if(sortedWord not in anagrams):
                anagrams[sortedWord] = []
            
            anagrams[sortedWord].append(word)
            
        return list(anagrams.values())


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