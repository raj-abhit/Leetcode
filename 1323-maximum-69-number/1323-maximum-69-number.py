class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        x = list(str(num))
        for i in range(len(x)):
            if x[i]  == "6":
                x[i] = "9"
                break
        num = int("".join(x))

        return num