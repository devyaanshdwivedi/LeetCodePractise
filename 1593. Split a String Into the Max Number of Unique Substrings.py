class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # DFS-based solution
        used = set()                                    # Working set of substrings
        max_distinct = 0                                # Best answer so far

        def propose(start, n):
            # DFS helper
            nonlocal max_distinct
            if start == len(s):                         # Stop recursion
                if n > max_distinct:                    # Adjust max if appropriate
                    max_distinct = n
            else:
                for i in range(start + 1, len(s) + 1):  # i is the substring end (+1)
                    candidate = s[start:i]
                    if candidate not in used:           # Unique so far, so legal
                        used.add(candidate)             # Add to set
                        propose(i, n + 1)               # Go deeper; next substring
                        used.remove(candidate)          # Remove (backtracking)

        propose(0, 0)                                   # Start here
        return max_distinct