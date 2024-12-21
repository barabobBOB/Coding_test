class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0

        for i in range(len(nums)):
            if nums[idx] == nums[i]:
                continue
            if nums[idx] != nums[i]:
                idx += 1
                nums[idx], nums[i] = nums[i], nums[idx]
    
        return idx + 1