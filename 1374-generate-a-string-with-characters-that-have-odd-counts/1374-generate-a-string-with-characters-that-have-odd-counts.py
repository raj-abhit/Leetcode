class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n%2 !=0:
            return n*"a"

        else:
            return (n-1)*"a"+"b"

        