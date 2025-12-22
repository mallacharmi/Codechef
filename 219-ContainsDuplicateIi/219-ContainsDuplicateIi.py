# Last updated: 12/22/2025, 5:24:38 PM
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        
        for i, num in enumerate(nums):
            if num in index_map:
                if i - index_map[num] <= k:
                    return True
            index_map[num] = i
        
        return False
