class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        count = 0
        char_count = Counter(chars)

        for word in words:

            word_count = Counter(word)

            for ch in word_count:
                if word_count[ch] > char_count[ch]:
                    break
            else:
                count += len(word)
        return count

        