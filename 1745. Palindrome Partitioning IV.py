class Solution:
    def checkPartitioning(self, s: str) -> bool:
        N = len(s)
        A = list(s)
        # initialize dp (On^2)
        dp = [[False] * N for _ in range(N)]
        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                dp[i][j] = (A[i] == A[j]) and (j - i < 2 or dp[i + 1][j - 1])
        # find in dp if all three substrings are palindrome, worst case O(N^2)
        for i in range(1, N - 1):
            if dp[0][i - 1]:
                for j in range(i, N - 1):
                    if dp[i][j] and dp[j + 1][N - 1]:
                        return True
        return False