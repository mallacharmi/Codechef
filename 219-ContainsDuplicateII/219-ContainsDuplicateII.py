# Last updated: 12/18/2025, 7:05:27 PM
1from typing import List
2
3class Solution:
4    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
5        index_map = {}
6        
7        for i, num in enumerate(nums):
8            if num in index_map:
9                if i - index_map[num] <= k:
10                    return True
11            index_map[num] = i
12        
13        return False
14