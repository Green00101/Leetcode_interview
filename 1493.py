class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest, pre, curr = 0,0,0
        for i in nums:
            if i:
                curr +=1
                longest = max(longest, pre+curr)
            else:
                pre,curr=curr,0
        return longest-(longest==len(nums))
