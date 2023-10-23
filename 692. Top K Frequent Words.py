class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        l = [(v,k) for k,v in Counter(words).items()]
        l.sort(key=lambda x:(-x[0], x[1]))
        return [w for f,w in l[:k]]