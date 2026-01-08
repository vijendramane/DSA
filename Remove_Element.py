 class Solution(object):
    def removeElement(self, nums, val):
        left = 0
        right = len(nums)

        while left < right: 
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1 S
                

        return right
