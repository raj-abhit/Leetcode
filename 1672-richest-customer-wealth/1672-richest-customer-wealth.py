class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        highest = 0
        
        rows = len(accounts)
        cols = len(accounts[0])

        for i in range(rows):
            total = 0
            for j in range(cols):
                total += accounts[i][j] 
            
            
            highest = max(total,highest)
            

        return highest