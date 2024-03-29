# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        while start < end:
            m = (start+end) // 2
            if isBadVersion(m):
                end = m
            else: 
                start = m + 1
        return start