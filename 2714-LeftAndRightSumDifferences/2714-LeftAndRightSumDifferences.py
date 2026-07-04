# Last updated: 7/4/2026, 7:05:02 PM
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        answer = [0] * n

        # left sum
        for i in range(1, n):
            leftSum[i] = leftSum[i-1] + nums[i-1]

        # right sum
        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]

        # answer
        for i in range(n):
            answer[i] = abs(leftSum[i] - rightSum[i])

        return answer
