class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        cur = max_sum
        for i in range(k,len(nums)):
            cur += nums[i]
            cur -= nums[i - k]

            max_sum = max(max_sum, cur)
        return max_sum / k
