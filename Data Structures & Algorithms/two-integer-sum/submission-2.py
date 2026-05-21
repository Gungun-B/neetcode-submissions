class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i, j]
        
        count = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in count:
                return [count[diff], i]
            else:
                count[nums[i]] = i

        