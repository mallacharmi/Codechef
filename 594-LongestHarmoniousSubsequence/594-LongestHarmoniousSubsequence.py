# Last updated: 12/18/2025, 6:34:38 PM
1from collections import Counter
2from typing import List
3
4class Solution:
5    def findLHS(self, nums: List[int]) -> int:
6        freq = Counter(nums)
7        ans = 0
8        
9        for x in freq:
10            if x + 1 in freq:
11                ans = max(ans, freq[x] + freq[x + 1])
12        
13        return ans
14