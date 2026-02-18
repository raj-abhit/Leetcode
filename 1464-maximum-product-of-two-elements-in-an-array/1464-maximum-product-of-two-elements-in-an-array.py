class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        n=len(nums)
        
        result=(nums[n-1]-1)*(nums[n-2]-1)

        return result