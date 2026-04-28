class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = {}
        for num in nums:
            if num in new: 
                new[num] +=1
            else:
                new[num] = 1
        for num in new:
            if new[num] > 1:
                return num
        