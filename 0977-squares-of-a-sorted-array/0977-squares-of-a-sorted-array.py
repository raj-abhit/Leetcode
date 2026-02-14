class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        square = []
        

        for num in nums:
            square.append(num*num)

        square.sort()
        return square
