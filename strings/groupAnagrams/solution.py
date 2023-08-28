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

