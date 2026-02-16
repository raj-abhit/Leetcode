class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        error = 0

        for i in range(len(heights)):
            if heights[i]!= expected[i]:
                error += 1

        return error
