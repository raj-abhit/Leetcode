class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        new = {}
        ch =0
        for num in arr:
            if num in new:
                new[num]+=1
            else:
                new[num] = 1
        for num in new:
            if num == new[num]:
                ch = num
        if ch > 0:
            return ch
        return -1
        