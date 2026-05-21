class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
                return False

        temp = list(s)
        temp2 = list(t)
        for i in range(len(s)):
            if temp[i] in temp2:
                temp2.remove(temp[i])

        if len(temp2) == 0:
            return True
        else:
            return False


        