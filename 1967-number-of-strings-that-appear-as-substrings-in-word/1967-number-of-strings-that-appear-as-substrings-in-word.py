class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count =0
        for w in patterns:
            if w in word:
                count += 1
        return count


        