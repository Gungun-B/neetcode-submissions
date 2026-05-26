class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_ele, res = {}, []
        for ele in nums:
            count_ele[ele] = count_ele.get(ele, 0) + 1

        for i in range(k):
            num = max(count_ele, key = count_ele.get)
            res.append(num)
            count_ele.pop(num)

        return res

