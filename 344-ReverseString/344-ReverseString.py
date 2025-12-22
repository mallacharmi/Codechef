# Last updated: 12/22/2025, 5:20:52 PM
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6        a=0
7        b=len(s)-1
8        while a<b:
9            s[a],s[b]=s[b],s[a]
10            a+=1
11            b-=1
12        
13        