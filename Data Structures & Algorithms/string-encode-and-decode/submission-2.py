class Solution:

    # def encode(self, strs: List[str]) -> str:
    #     s = ",".join(strs)
    #     return s

    # def decode(self, s: str) -> List[str]:
    #     strs = s.split(",")
    #     return strs
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            # Append length and a delimiter # before the string
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Find the delimiter '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the length
            length = int(s[i:j])
            
            # Extract the string using the length
            # Start after '#', take 'length' characters
            res.append(s[j+1 : j+1+length])
            
            # Move index to the start of the next string
            i = j + 1 + length
            
        return res
        

