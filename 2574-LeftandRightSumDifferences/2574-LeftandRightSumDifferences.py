# Last updated: 12/28/2025, 1:59:21 PM
1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        leftSum = [0] * n
5        rightSum = [0] * n
6        answer = [0] * n
7
8        # left sum
9        for i in range(1, n):
10            leftSum[i] = leftSum[i-1] + nums[i-1]
11
12        # right sum
13        for i in range(n-2, -1, -1):
14            rightSum[i] = rightSum[i+1] + nums[i+1]
15
16        # answer
17        for i in range(n):
18            answer[i] = abs(leftSum[i] - rightSum[i])
19
20        return answer
21