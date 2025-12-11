 class Solution(object):
    def romanToInt(self, s):
        values = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev = 0 
        
        for ch in reversed(s):  # loop from right to left
            val = values[ch]
            
            if val < prev:
                total -= val
            else:
                total += val
            
            prev = val
        
        return total
