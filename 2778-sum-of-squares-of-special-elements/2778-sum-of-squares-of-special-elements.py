class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        special = 0
        n = len(nums)
        for i  in range(n):
            if n%(i+1) ==0:

                special = special+(nums[i]*nums[i])

        return special
        
        