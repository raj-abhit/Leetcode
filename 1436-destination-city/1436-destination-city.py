class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        sources = set()
        for src,dst in paths:
            sources.add(src)

        for src, dst in paths:
            if dst not in sources:
                return dst