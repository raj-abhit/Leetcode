class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nom = sorted(nums)
        n = len(nums)
        if nom[n-1]>=2*nom[n-2]:
            for i in range(n):
                if nums[i] == nom[n-1]:
                    return i

        return -1


        