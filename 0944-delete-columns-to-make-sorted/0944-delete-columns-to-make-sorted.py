class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        row = len(strs)
        col = len(strs[1])
        delete = 0

        for j in range(col):
            for i in range(1,row):
                if strs[i][j] < strs[i-1][j]:
                    delete += 1
                    break
        return delete
