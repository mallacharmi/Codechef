# Last updated: 8/20/2025, 5:42:14 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_can=max(candies)
        res=[]
        for i in range(len(candies)):
            res.append(candies[i]+extraCandies>=max_can)
        return res
        