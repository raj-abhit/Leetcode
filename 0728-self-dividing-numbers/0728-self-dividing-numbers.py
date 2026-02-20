class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for num in range(left,right+1):
            original = num
            is_valid = True

            while num>0:
                digit = num % 10

                if digit == 0  or original % digit != 0:
                    is_valid = False
                    break

                num //= 10

            
            if is_valid:
                result.append(original)

        return result
                