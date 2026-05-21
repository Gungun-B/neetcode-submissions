class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tup = set(nums)
        if len(tup) == len(nums):
            return False
        else:
            return True
        