class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = 0
        count = 0
        for num in nums:
            if num ==1:
                count +=1
                maximum = max(maximum,count)
            else:
                count = 0

            
        return maximum

        
