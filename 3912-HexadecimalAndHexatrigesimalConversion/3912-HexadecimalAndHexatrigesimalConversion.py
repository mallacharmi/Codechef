# Last updated: 8/20/2025, 5:41:35 PM
class Solution:
    def concatHex36(self, n: int) -> str:
        hex_part = format(n * n, 'X')         # Convert n^2 to hexadecimal (base-16, uppercase)
        base36_part = self.to_base36(n * n * n)  # Convert n^3 to base-36 (hexatrigesimal)
        return hex_part + base36_part

    def to_base36(self, num: int) -> str:
        if num == 0:
            return "0"
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while num > 0:
            result = digits[num % 36] + result
            num //= 36
        return result
