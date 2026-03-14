class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        x=''
        y=''
        for w in word1:
            x +=w
        for w in word2:
            y+=w
     

        if x == y:
            return True
        return False

        