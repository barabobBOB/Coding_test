class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx = 0
        for n in nums2:
            nums1[m+idx] = n
            idx += 1
        
        print(nums1.sort())