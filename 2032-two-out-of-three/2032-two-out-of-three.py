class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        common = []
        new =  set(nums1 + nums2 + nums3)
        for num in new:
            if num in nums1 and num in nums2:
                common.append(num)
            elif num in nums1 and num in nums3:
                common.append(num)
            elif num in nums2 and num in nums3:
                common.append(num)


        

        return common