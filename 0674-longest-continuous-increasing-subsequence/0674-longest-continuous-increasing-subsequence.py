class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = 1
        count = 1
        for i in range(1,len(nums)):
            if nums[i]> nums[i-1]:
                count += 1
                maximum = max(maximum,count)
            else:
                count = 1
        return maximum

        