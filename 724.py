class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls = 0
        rs = sum(nums)
        for idx, ele in enumerate(nums):
            rs-= ele
            if rs == ls:
                return idx
            else:
                ls+= ele
        return -1
