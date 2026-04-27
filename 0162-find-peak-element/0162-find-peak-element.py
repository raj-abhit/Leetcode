class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if len(nums)  == 1:
                return 0
            elif nums[0] > nums[1]:
                return 0
            elif nums[len(nums)-1] > nums[len(nums)-2]:
                return len(nums) -1
            if nums[i]> nums[i-1] and nums[i]> nums[i+1]:
                return i

            
        