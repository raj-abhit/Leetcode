class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        target = ord(target)
        letters = [ord(ch) for ch in letters]
        letters.sort()

        for i in range(len(letters)):
            if letters[i]>target:
                return chr(letters[i])
            
        return chr(letters[0])

    
        