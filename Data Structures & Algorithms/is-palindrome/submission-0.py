class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = "".join(char for char in s if char.isalnum()).lower()
        
        l = len(palin)//2

        for i in range(l):
            r = len(palin)-1-i
            if palin[i] != palin[r]:
                return False
            else:
                r -= 1
        return True