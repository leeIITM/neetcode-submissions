from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2  # Recalculated every iteration
            
            if nums[mid] == target:
                return mid  # Target found, exit immediately
            elif nums[mid] < target:
                left = mid + 1  # Move right, bypasses the stuck-loop issue
            else:
                right = mid - 1  # Move left, bypasses the stuck-loop issue
                
        # If target is not found, 'left' will naturally hold the insertion index
        return left
        