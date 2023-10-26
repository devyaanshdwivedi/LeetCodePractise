class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg = sum(1 for x in matrix for x in x if x < 0)
        if neg % 2 == 0:
            return sum(abs(x) for x in matrix for x in x)
        else:
            return sum(abs(x) for x in matrix for x in x) - 2 * abs(min((x for x in matrix for x in x),key=abs))s