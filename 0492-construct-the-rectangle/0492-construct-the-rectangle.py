class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        """for i in range(2,area-1):
            if area %i == 0:
                return [area//i,i]

            else:
                return [area,1]
 mid = area//2
        

        for i in range(mid , 0,-1):
            for j in range(i,0,-1):
                if i*j== area:
                    return [i,j]
                
        return [area,1]
"""


        best = [area,1]
        minimum = area

        for w in range(1,area+1):
            if area% w ==0:
                l = area//w

                if l >= w and (l-w)< minimum:
                    minimum = l-w
                    best = [l,w]

        return best
