class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        new = {}
        on = []

        for i in range(len(bulbs)):
            if bulbs[i] in new:
                new[bulbs[i]]+= 1
            else:
                new[bulbs[i]] = 1

        for bulb  in  new:
            if new[bulb]%2 != 0:
                on.append(bulb)

        return sorted(on)