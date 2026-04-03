class Solution(object):
    def earliestTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        smallest = float('inf')
        for s,t in tasks:
            if s+t < smallest:
                smallest = s+t
        return smallest

        