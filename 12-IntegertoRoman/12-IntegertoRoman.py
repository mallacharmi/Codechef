# Last updated: 1/2/2026, 8:53:44 PM
1class Solution:
2    def intToRoman(self, num: int) -> str:
3        roman_map = [
4            (1000, "M"),
5            (900, "CM"),
6            (500, "D"),
7            (400, "CD"),
8            (100, "C"),
9            (90, "XC"),
10            (50, "L"),
11            (40, "XL"),
12            (10, "X"),
13            (9, "IX"),
14            (5, "V"),
15            (4, "IV"),
16            (1, "I")
17        ]
18        
19        result = ""
20        
21        for value, symbol in roman_map:
22            while num >= value:
23                result += symbol
24                num -= value
25        
26        return result
27