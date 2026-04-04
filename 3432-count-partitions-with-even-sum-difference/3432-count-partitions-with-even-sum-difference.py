class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total =  sum(nums)
        left = 0
        count = 0

        for i in  range(len(nums)-1):
            left += nums[i]
            total -= nums[i]
            
            if (total - left) %2 == 0:
                count +=1
        return count

            