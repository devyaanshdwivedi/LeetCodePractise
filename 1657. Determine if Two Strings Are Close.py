from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        frequency1 = Counter(word1)
        frequency2 = Counter(word2)
        if set(frequency1.keys()) != set(frequency2.keys()):
            return False
        frequency1 = dict(sorted(frequency1.items(), key=lambda item: item[1]))
        frequency2 = dict(sorted(frequency2.items(), key=lambda item: item[1]))
        return [frequency for frequency in frequency1.values()] == [frequency for frequency in frequency2.values()]