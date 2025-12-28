# Last updated: 12/28/2025, 1:39:59 PM
1class Solution:
2    def largestAltitude(self, gain: List[int]) -> int:
3        prefix=[0]*(len(gain)+1)
4        prefix[0]=gain[0]
5        for i in range(0,len(gain)):
6            prefix[i]=prefix[i-1]+gain[i]
7        return max(prefix)
8
9