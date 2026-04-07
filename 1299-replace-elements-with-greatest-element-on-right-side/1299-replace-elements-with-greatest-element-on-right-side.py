class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        """new = []
        for i in range(len(arr)):
            if  i == len(arr) - 1:
                new.append(-1)
            else:
                new.append(max(arr[i+1:])  )

        return new      """
        max_right = -1
        for i in range(len(arr) -1,-1,-1):
            temp = arr[i]
            arr[i] = max_right
            max_right = max(max_right,temp)

        return arr