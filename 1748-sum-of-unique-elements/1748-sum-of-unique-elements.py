class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = {}

        for num in nums:
            if num in new:
                new[num] += 1
            else:
                new[num] = 1
        total = 0
        for num in new:
            if new[num] ==1:
                total += num

        return total
