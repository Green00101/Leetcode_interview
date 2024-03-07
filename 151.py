class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = reversed(s)
        return ' '.join(s)
