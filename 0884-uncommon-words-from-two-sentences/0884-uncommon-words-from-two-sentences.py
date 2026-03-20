class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        new = {}
        words = s1.split() + s2.split()

        for word in words:
            if word in new:
                new[word] += 1
            else:
                new[word] = 1

        x= []
        for word in new:
            if new[word] ==1:
                x.append(word)

        return x