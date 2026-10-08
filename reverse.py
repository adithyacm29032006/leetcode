class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        
        while x != 0:
            res = res * 10 + x % 10
            x //= 10
            
        res *= sign
        if res < -2147483648 or res > 2147483647:
            return 0
            
        return res
