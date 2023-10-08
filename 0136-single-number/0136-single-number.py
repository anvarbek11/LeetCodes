class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b = 0
        for i in nums:
            b = b ^ i
        return b   