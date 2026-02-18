class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        arr = sorted(arr)
        target = sorted(target)

        for i in range(len(target)):
            if arr[i] != target[i]:
                return False

        return True

