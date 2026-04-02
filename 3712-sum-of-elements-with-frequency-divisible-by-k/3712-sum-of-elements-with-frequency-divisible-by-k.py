class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        new = {}
        for num in nums:
            if num in new:
                new[num] += 1
            else:
                new[num] = 1
        res =  0
        for num in new:
            if new[num]%k == 0:
                res += new[num]*num
        return res