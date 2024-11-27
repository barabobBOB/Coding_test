class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_nums = len(nums) - 1

        for i in range(len_nums + 1):
            if len_nums == i and nums[i] != val:
                break

            if nums[i] == val:
                while nums[len_nums] == val:
                    if len_nums == i:
                        break
                    nums[len_nums] = "_"
                    len_nums -= 1

                nums[i] = "_"
                nums[len_nums], nums[i] = nums[i], nums[len_nums]
                len_nums -= 1

        return len_nums + 1