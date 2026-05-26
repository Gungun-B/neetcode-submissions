class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_res = {}
        res = []
        for ind, s in enumerate(strs):
            sorted_str = "".join(sorted(s))
            if sorted_str not in strs_res:
                strs_res[sorted_str] = [s]
            else:
                strs_res[sorted_str].append(s)

        for value in strs_res.values():
            res.append(value)

        return res