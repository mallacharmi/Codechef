# Last updated: 8/20/2025, 5:43:24 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)   
            count += 1
        return count