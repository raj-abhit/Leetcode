class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        low = 0
        high = len(s) 
        prem = []

        for i in range(len(s)):
            if s[i] == "I":
                prem.append(low)
                low = low+1
            else:
                prem.append(high)
                high -=1
        prem.append(low)
        return prem



        