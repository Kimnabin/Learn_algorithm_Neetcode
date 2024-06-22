class Solution:
    
    def __init__(self, nums):
        self.nums = nums
        self.longest = 0
    
    
    def longestCunsecutive(self, nums):
        nums = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 not in nums:
                current_num = num
                current_length = 1
                
                while current_num + 1 in nums:
                    current_num += 1
                    current_length += 1
                    
                longest = max(longest, current_length)
                
        return longest
    
    
nums = [100, 4, 200, 1, 3, 2]

s = Solution(nums).longestCunsecutive(nums)

print(s)