# Last updated: 8/20/2025, 5:41:47 PM

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if num % 3 != 0:
                count += 1
        return count