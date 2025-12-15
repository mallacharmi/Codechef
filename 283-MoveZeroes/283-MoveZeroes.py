# Last updated: 12/15/2025, 5:59:40 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        left=0
7        for right in range(len(nums)):
8            if nums[right]!=0:
9                nums[left],nums[right]=nums[right],nums[left]
10                left+=1
11        