class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)

        for i in range(n-1,1,-1):
            if nums[i-2]+nums[i-1]>nums[i]:
                return  nums[i-1]+nums[i-2]+nums[i]

            

        return 0
        