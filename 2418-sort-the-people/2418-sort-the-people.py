class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        """new = {}
        
        for i in range(len(heights)):
            new[names[i]] = heights[i]
            

        

        new = sorted(new, key= lambda x:new[x],reverse = True)
        return new"""

        return [name for _,name in sorted(zip(heights,names),reverse = True)]