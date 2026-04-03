class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        new= []
        for num in order:
            if num in friends:
                new.append(num)

        return new
