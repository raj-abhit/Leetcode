class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = []
        for num in nums:
            if num%3  ==  0 and num%2 ==0:
                new.append(num)
        total = 0
        average = None

        for num in new:
            total += num

        if len(new) > 0:
            average = total//len(new)
        else:
            return 0

        return average
