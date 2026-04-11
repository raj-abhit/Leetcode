class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x<0 else 1

        reverse_str = int(str(abs(x))[::-1])*sign

        if reverse_str< -2**31 or reverse_str>2**31:
            return 0
        return reverse_str

