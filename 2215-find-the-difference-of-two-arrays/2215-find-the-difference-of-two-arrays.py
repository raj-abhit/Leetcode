class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        n = set()
        m = set()

        for num in nums1:
            if num not in nums2:
                n.add(num)

        for num in nums2:
            if num not in nums1:
                m.add(num)

        

        return [list(n),list(m)]

        