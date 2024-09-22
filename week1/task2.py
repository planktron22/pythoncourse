class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""        
        maxpal = ""
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(maxpal):
                    maxpal = s[l:r + 1]
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(maxpal):
                    maxpal = s[l:r + 1]
                l -= 1
                r += 1

        return maxpal

sol = Solution()
s = input()
print(sol.longestPalindrome(s))