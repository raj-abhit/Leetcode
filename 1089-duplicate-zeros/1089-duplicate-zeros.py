class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        new = []

        for i in range(n):
            if arr[i] == 0:
                new.append(0)
                new.append(0)

            else:
                new.append(arr[i])
        for i in range(n):
            arr[i] = new[i]
        return arr


   


                    