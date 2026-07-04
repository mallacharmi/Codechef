# Last updated: 7/4/2026, 7:05:57 PM
class Solution:
    def generate(self, numRows: int):
        triangle = []

        for row in range(numRows):
            # create row with all 1s
            curr = [1] * (row + 1)

            # fill middle elements
            for col in range(1, row):
                curr[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]

            triangle.append(curr)

        return triangle
