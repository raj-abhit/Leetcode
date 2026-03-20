class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        """x = []
        for i in range(1,num//2+1):
            if num%i == 0:
                x.append(i)

        
        if sum(x) == num:
            return True
        return False"""
        if num <= 1:
            return False
        total = 1
        i = 2
        while i*i <= num:
            if num%i == 0:
                total += i
                if i != num//i:
                    total += num//i
            i+=1


        return total == num

        