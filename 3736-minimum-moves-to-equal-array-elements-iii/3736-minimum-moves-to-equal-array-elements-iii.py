class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        moves = 0

        for num in nums:
            if num < m:
                moves += m-num
        return moves
