class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxA = 0
        curr = 0
        for g in gain:
            curr += g
            maxA = max(maxA, curr)
        return maxA
