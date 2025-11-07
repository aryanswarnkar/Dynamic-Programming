class Solution:
    # Function to return the LCS string of text1 and text2
    def longestCommonSubsequence(self, text1: str, text2: str) -> str:
        n, m = len(text1), len(text2)

        # Create DP table to store lengths of LCS for all substrings
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill dp table bottom-up
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Characters match: increase length by 1
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # Characters don't match: take max of left and top
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Reconstruct LCS string from dp table
        i, j = n, m
        lcs = []

        # Traverse dp table from bottom-right to top-left
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                # Characters match, add to result and move diagonally
                lcs.append(text1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                # Move up if top cell has greater value
                i -= 1
            else:
                # Move left otherwise
                j -= 1

        # Reverse list since it was built backwards
        return ''.join(reversed(lcs))


if __name__ == "__main__":
    s1 = "abcde"
