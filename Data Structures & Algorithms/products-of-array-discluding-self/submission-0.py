class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod = 1
        # result = []
        # for i in nums:
        #     prod *= i
        # for num in nums:
        #     t = prod/num
        #     result.append(t)
        # return result

        n = len(nums)
        res = [1 for i in range(n)]
        left_prod, right_prod = 1, 1

        for l in range(n):
            res[l] = left_prod
            left_prod *= nums[l]

        for r in range(n-1, -1, -1):
            res[r] *= right_prod
            right_prod *= nums[r]

        return res



        