class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = frozenset("aeiou")
        cur = ans = sum(s[i] in vowels for i in range(k))
        for i in range(k,len(s)):
            cur += (s[i] in vowels) - (s[i-k] in vowels)
            ans = max(cur,ans)
        return ans
