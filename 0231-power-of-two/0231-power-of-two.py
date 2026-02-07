class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n%2 == 0:
            n= n//2

        if n ==1:
            return True

        else:
            return False

        #return n==1 same as above if else loop of return