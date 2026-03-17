class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        new = {}
        for ch in arr:
            if ch in new:
                new[ch] +=1
            else:
                new[ch] = 1
        x = []
        for ch in arr:
            if new[ch]==1:
                x.append(ch)
        
        if k<= len(x):
            return x[k-1]

        return ""