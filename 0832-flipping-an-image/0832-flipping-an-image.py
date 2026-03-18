class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols  = len(image[0])

        for i in range(rows):
            for j in range(cols):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0

        for i in range(rows):
            image[i].reverse()

        return image
        