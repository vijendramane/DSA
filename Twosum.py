 class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # Dictionary to store numbers and their indices
        
        for i, num in enumerate(nums):
            complement = target - num  # Find the complement
             
            if complement in num_map:
                return [num_map[complement], i]  # Return indices
            
            num_map[num] = i  # Store index of current number
        
        return []  # As per problem constraints, this won't be reached
