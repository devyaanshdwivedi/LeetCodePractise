import random
from itertools import permutations
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums
        self.combinations = permutations(nums)
        self.random = random.Random()

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        try:
            return next(self.combinations)
        except StopIteration:
            self.combinations = permutations(self.reset())
            return next(self.combinations)