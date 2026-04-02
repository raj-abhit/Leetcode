class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = max(nums)
        n = min(nums)
        missing = []

        for i in range(n,m):
            if i not in  nums:
                missing.append(i)
        return missing
        