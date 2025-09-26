def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # Create a DP table of size (n+1) x (m+1) initialized with -1
    dp = [[-1 for j in range(m + 1)] for i in range(n + 1)]

    # Initialize the base cases:
    # - The length of LCS with an empty string is 0, so dp[i][0] = 0 for all i
    # - The length of LCS with an empty string is 0, so dp[0][j] = 0 for all j
    for i in range(n + 1):
        dp[i][0] = 0
    for j in range(m + 1):
        dp[0][j] = 0

    # Fill in the DP table by considering characters from both strings
    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                # If the characters match, increment the LCS length
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            else:
                # If the characters do not match, take the maximum of
                # LCS length without one character from s1 or s2
                dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])
    
    # The value in dp[n][m] represents the length of the Longest Common Subsequence
    return dp[n][m], dp


def main():
    s1 = "ABCXYD"
    s2 = "AWXCDY"
    length, dp = lcs(s1, s2)

    for row in dp:
        print(row)

    print("O tamanho da maior subsequência comum é", length)

if __name__ == "__main__":
    main()