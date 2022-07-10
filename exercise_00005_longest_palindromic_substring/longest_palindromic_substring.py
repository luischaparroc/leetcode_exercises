

def longestPalindrome(s: str) -> str:
    if s == "":
        return s

    res = ""
    dp = [None for _ in range(len(s))]

    for j in range(len(s)):
        for i in range(j + 1):
            if i == j:
                dp[i] = True
            elif j == i + 1:
                dp[i] = (s[i] == s[j])
            else:
                dp[i] = (dp[i + 1] and s[i] == s[j])
            if dp[i] and j - i + 1 > len(res):
                res = s[i:j + 1]

    return res
