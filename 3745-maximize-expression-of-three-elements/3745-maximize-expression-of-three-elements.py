class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        """a = max(nums)
        b = nums[n-2]
        c = min(nums)

        total = a+b-c"""
        total = max(nums) + nums[n-2] - min(nums)

        return total

        