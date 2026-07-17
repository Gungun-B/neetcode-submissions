class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #  nums = [20, 4, 10, 3, 4, 5, 2]

        nums_seq = set(nums)
        longest_seq = 0
        for num in nums_seq:
            if num - 1 not in nums_seq:
                count = 1
                seq = num
                
                while seq + 1 in nums_seq:
                    seq += 1
                    count += 1
                    
                longest_seq = max(count, longest_seq)
        return longest_seq
        
        
        


        
        