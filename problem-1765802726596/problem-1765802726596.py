# Last updated: 12/15/2025, 6:15:26 PM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        res = []
5
6        for i in range(len(nums)):
7            if i > 0 and nums[i] == nums[i - 1]:
8                continue
9
10            left, right = i + 1, len(nums) - 1
11
12            while left < right:
13                total = nums[i] + nums[left] + nums[right]
14
15                if total == 0:
16                    res.append([nums[i], nums[left], nums[right]])
17                    left += 1
18                    right -= 1
19
20                    while left < right and nums[left] == nums[left - 1]:
21                        left += 1
22                    while left < right and nums[right] == nums[right + 1]:
23                        right -= 1
24
25                elif total < 0:
26                    left += 1
27                else:
28                    right -= 1
29
30        return res
31