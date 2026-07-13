class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}
        for ind, ele in enumerate(numbers, start=1):
            temp = target - ele
            if temp in m and (m[temp] < ind and temp != ele):
                return [m[temp], ind]
            else:
                m[ele] = ind

        