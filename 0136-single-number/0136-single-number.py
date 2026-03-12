class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = set(nums)
        
        unique = sum(new)*2 - sum(nums)

        return unique