class Solution(object):
        """
        :type x: int
        :rtype: bool
        """
        def isPalindrome(self , x):
            s = str(x)
            return s == s[::-1]
