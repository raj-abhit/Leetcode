class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = []
        for i in range(len(nums)):
            if i%10 == nums[i]:
                new.append(i)
        if new:
            return min(new)
        else:
            return -1
        