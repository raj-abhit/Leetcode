class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count =0
        for w in words:
            valid = True

            for c in w:
                if c not in allowed:
                    valid = False

            if valid == True:
                count += 1
        return count

        