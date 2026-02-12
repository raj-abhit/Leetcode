class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        expected = 0
        for i in range(n+1):
            expected +=i

        actual = sum(nums)
        missing = expected - actual
        return missing
        