class Solution:
    def numMatchingSubseq(self, s: str, words) -> int:
        """
        Given a string of lowercase letters (s) and an array
        of words (words), this program determines the number
        of words that are a subsequence of s.

        :param s: string of lowercase letters
        :type s: str
        :param words: array of words
        :type words: list[str]
        :return: number of words that are a subsequence of s
        :rtype: int
        """
        matches = 0
        for word in words:
            start = 0
            found = True
            for char in word:
                location = s.find(char, start)
                if location == -1:
                    found = False
                    break
                start = location + 1
            if found:
                matches += 1
        return matches