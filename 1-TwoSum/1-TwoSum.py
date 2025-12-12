# Last updated: 12/12/2025, 7:00:51 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        hashmap = {}  # Stores value: index
4        for i, num in enumerate(nums):
5            complement = target - num
6            if complement in hashmap:
7                return [hashmap[complement], i]
8            hashmap[num] = i