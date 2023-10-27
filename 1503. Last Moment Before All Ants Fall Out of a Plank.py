class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if left == [] and right == []:
            return 0
        if left == []:
            return n - min(right)
        if right == []:
            return max(left)
        return max(max(left), n-min(right))