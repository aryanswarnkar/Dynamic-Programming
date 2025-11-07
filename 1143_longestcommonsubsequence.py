class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        def lcsUtil(s1, s2, ind1, ind2, dp):
            # Base case: If either of the strings has reached the end
            if ind1 < 0 or ind2 < 0:
                return 0
            
            # If the result for this state is already calculated, return it
            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]
            
            # If the characters at the current indices match, include them in the LCS
            if s1[ind1] == s2[ind2]:
                dp[ind1][ind2] = 1 + lcsUtil(s1, s2, ind1 - 1, ind2 - 1, dp)
            else:
                # If the characters do not match, consider both possibilities:
                # 1. Exclude character from s1 and continue matching in s2
                # 2. Exclude character from s2 and continue matching in s1
                dp[ind1][ind2] = max(lcsUtil(s1, s2, ind1, ind2 - 1, dp), lcsUtil(s1, s2, ind1 - 1, ind2, dp))
            
            return dp[ind1][ind2]

        n = len(s1)
        m = len(s2)
        dp = [[-1 for j in range(m)] for i in range(n)]
        return lcsUtil(s1, s2, n - 1, m - 1, dp)
