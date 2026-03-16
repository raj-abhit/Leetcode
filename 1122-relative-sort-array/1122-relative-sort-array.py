class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        new = {}
        remaining =[]
        arr3=[]
        for num in arr1:
            if num in new:
                new[num] += 1
            else:
                new[num] = 1
        for num in arr2:
            while new[num]>0:
                arr3.append(num)
         
                new[num]-=1
        for num in new:
            while new[num]>0:
                remaining.append(num)
                new[num] -= 1
        remaining.sort()
        return arr3 + remaining       