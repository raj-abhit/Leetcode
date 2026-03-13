class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        new = []
        total = None
        for i in range(n):
            if i == 0:
                total = nums[0]
            else:
                total = nums[i]+total

            new.append(total)

        return new
