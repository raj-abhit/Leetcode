class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small = []
        
        for i in range(len(nums)):
            
            if i == sum(int(d)for d in str(nums[i])):

                return i

        return -1
                

        