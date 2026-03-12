class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        total = 0
        n= len(mat)

        for i in range(n):
            total += mat[i][i]
            total += mat[i][n-i-1]


        if n%2 ==1:
            total -= mat[n//2][n//2]

        return total


