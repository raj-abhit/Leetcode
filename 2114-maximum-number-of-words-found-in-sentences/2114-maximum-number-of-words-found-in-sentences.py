class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maxi = 0
        for s in sentences:
            words = len(s.split())
            maxi = max(words,maxi)
        return maxi