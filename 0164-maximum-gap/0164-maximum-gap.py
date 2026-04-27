class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        x = 0
        for i in range(n-1):
            x = max(x,nums[i+1]-nums[i])

        return x