class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        n = len(nums)
        for i in range(n-1):
            if i+1 != nums[i]:
                return False

        if nums[n-1] == n-1:
            return True

        return False

       
        