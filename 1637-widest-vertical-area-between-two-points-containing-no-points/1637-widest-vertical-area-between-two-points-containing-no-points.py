class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x = sorted(p[0] for p in points)

        maxgap= 0

        for i in range(1,len(x)):
            gap = x[i] - x[i-1]

            maxgap = max(maxgap,gap)
        return maxgap
