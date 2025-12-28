# Last updated: 12/28/2025, 1:28:59 PM
1class Solution:
2    def largestAltitude(self, gain: List[int]) -> int:
3        prefix=[0]*(len(gain)+1)
4        prefix[0]=0
5        for i in range(1,len(gain)):
6            prefix[i]=prefix[i-1]+nums[i]
7        return max(prefix)
8class Solution:
9    def largestAltitude(self, gain: List[int]) -> int:
10        altitude = 0
11        max_altitude = 0
12        
13        for g in gain:
14            altitude += g
15            max_altitude = max(max_altitude, altitude)
16        
17        return max_altitude
18