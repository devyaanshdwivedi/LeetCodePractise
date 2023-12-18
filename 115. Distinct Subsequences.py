class Solution:
    def recursiveWithoutMemoization(self, s: str, t: str, s_ind: int, t_ind: int) -> int:
        if t_ind == len(t):
            return 1
        if s_ind == len(s):
            return 0

        take, notTake = 0, 0

        if s[s_ind] == t[t_ind]:
            take = self.recursiveWithoutMemoization(s, t, s_ind + 1, t_ind + 1)

        notTake = self.recursiveWithoutMemoization(s, t, s_ind + 1, t_ind)

        return take + notTake

    def numDistinct(self, s: str, t: str) -> int:
        return self.recursiveWithoutMemoization(s, t, 0, 0)