class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        count = {}
        for i in range(len(nums)):
            if sorted_nums[i] not in count:
                count[sorted_nums[i]] = i

        result = []
        for i in range(len(nums)):
            result.append(count[nums[i]])

        return result

            