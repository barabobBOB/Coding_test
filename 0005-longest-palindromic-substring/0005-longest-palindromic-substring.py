class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''

        for i, j in enumerate(s):
            string = ''
            for k in range(i, len(s)):
                string += s[k]
                if string[0] == string[-1]:

                    if string == string[::-1] and len(result) < len(string):
                        result = string

        return result


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#         res = ""
        
#         # 모든 길이 1의 부분 문자열은 회문입니다.
#         for i in range(n):
#             dp[i][i] = True
#             res = s[i]
        
#         # 길이 2의 부분 문자열을 확인합니다.
#         for i in range(n - 1):
#             if s[i] == s[i+1]:
#                 dp[i][i+1] = True
#                 res = s[i:i+2]
        
#         # 길이 3 이상의 부분 문자열을 확인합니다.
#         for length in range(3, n+1):
#             for i in range(n - length + 1):
#                 j = i + length - 1
#                 if s[i] == s[j] and dp[i+1][j-1]:
#                     dp[i][j] = True
#                     if length > len(res):
#                         res = s[i:j+1]
        
#         return res
