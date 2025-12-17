# Last updated: 12/17/2025, 8:35:18 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        left, right = 0, len(s) - 1
4
5        while left < right:
6            # skip non-alphanumeric characters
7            while left < right and not s[left].isalnum():
8                left += 1
9            while left < right and not s[right].isalnum():
10                right -= 1
11
12            # compare characters
13            if s[left].lower() != s[right].lower():
14                return False
15
16            left += 1
17            right -= 1
18
19        return True
20