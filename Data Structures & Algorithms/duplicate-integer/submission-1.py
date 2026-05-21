class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_arr = set(nums)
        if len(nums) == len(dup_arr):
            return False
        else:
            return True
        