class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        new = []
        for i in range(rows):
            for j in range(cols):
                dist = abs(i-rCenter) +  abs(j-cCenter)
                new.append([dist,i,j])

        new.sort()

        return [[i,j] for dist,i,j in new]

        