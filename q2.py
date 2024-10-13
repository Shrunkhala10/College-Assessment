def min_operations(str1, str2):
    m, n = len(str1), len(str2)

  
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    
    lcs_length = dp[m][n]

    
    min_deletions = m - lcs_length
    min_insertions = n - lcs_length

    return min_deletions, min_insertions

str1 = "heap"
str2 = "pea"
deletions, insertions = min_operations(str1, str2)
print("Minimum Deletion =", deletions, "and Minimum Insertion =", insertions)
