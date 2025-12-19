# Last updated: 12/19/2025, 6:40:11 PM
1from typing import List
2
3class NumArray:
4
5    def __init__(self, nums: List[int]):
6        self.prefix = [0]
7        for num in nums:
8            self.prefix.append(self.prefix[-1] + num)
9
10    def sumRange(self, left: int, right: int) -> int:
11        return self.prefix[right + 1] - self.prefix[left]
12