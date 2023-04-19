class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        start_idx = 0
        end_idx = len(nums)
        
        while start_idx < end_idx:
            target_idx = (start_idx + end_idx) // 2
            
            if target <= nums[target_idx]:
                end_idx = target_idx
            else:
                start_idx = target_idx + 1
                
        return start_idx