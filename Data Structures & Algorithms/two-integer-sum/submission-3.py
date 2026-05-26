class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for ind, num in enumerate(nums):
            diff = target - num
            if diff in dic:
                return [dic[diff], ind]
            dic[num] = ind

        