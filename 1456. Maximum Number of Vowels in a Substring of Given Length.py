class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        left_gen, right_gen = (ch for ch in s), (ch for ch in s)

        cnt = 0
        for _ in range(k): cnt += next(right_gen) in vowels

        if cnt == k: return k
        return max(max(accumulate((new in vowels) - (old in vowels) for old, new in zip(left_gen, right_gen))), 0) + cnt