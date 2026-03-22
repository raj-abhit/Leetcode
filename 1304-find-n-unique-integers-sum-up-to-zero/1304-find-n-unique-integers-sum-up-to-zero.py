class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        new = []
        for i in range(1, (n//2 )+ 1):
            new.append(i)
            new.append(-i)

        if n%2 ==0:
            return new
        else:
            new.append(0)
        return new

        
        

        