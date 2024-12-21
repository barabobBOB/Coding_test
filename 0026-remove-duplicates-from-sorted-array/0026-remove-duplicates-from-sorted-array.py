class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        k = 1
        len_nums = len(nums)
        check = 0

        if len(nums) == 1:
            return k

        before_value = nums[0]

        for i in range(1, len_nums):
            if before_value == nums[i]:
                check += 1
            if before_value != nums[i]:
                before_value = nums[i]
                nums[idx] = nums[i]
                idx += 1
                k += 1
        
        if k == 1:
            if check == 0:
                return len_nums
            else:
                return 1
            
        return k