class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set_nums = set(nums)
        cnt = 0
        num = 0
        for i in set_nums:
            cnt_num = nums.count(i)
            if cnt < cnt_num:
                cnt = cnt_num
                num = i
        return num