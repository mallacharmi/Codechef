# Last updated: 12/26/2025, 5:16:15 PM
1class Solution:
2    def runningSum(self, nums: List[int]) -> List[int]:
3        prefix=[0]*len(nums)
4        prefix[0]=nums[0]
5        for i in range(1,len(nums)):
6            prefix[i]=prefix[i-1]+nums[i]
7        return prefix
8        