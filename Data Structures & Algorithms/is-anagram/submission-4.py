class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # S, T = list(s), list(t)
        # for i in range(len(s)):
        #     if S[i] in T:
        #         T.remove(S[i])
        #     else:
        #         return False
        # if len(T) == 0:
        #     return True
        # else:
        #     return False
        # ---------------
        #method 2
        # if len(s) != len(t):
        #     return False
        
        # return sorted(s) == sorted(t)

        # ---------------

        if len(s) != len(t):
            return False
        map = {}
        for i in s:
            map[i] = map.get(i, 0) + 1
        for i in t:
            map[i] = map.get(i, 0) - 1
        
        return all(ele == 0 for ele in map.values())


