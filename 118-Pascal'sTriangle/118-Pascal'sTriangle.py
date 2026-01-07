# Last updated: 1/7/2026, 8:29:45 PM
1class Solution:
2    def generate(self, numRows: int):
3        triangle = []
4
5        for row in range(numRows):
6            # create row with all 1s
7            curr = [1] * (row + 1)
8
9            # fill middle elements
10            for col in range(1, row):
11                curr[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
12
13            triangle.append(curr)
14
15        return triangle
16