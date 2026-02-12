class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        max1 = nums[n-1]* nums[n-2] * nums[n-3]
        max2 = nums[0] *nums[1] *nums[n-1]

        return max(max2,max1)