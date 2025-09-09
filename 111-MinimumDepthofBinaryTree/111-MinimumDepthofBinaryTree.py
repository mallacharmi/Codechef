# Last updated: 9/9/2025, 5:27:48 PM
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Queue stores (node, depth)
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            
            # Check if it's a leaf node
            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
