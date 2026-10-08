class Solution:
    def myAtoi(self, s):
        s = s.lstrip()
        if not s:
            return 0
            
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
            
        res = 0
        int_max = 2147483647
        int_min = -2147483648
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if res > int_max // 10 or (res == int_max // 10 and digit > 7):
                return int_max if sign == 1 else int_min
            res = res * 10 + digit
            i += 1
            
        return sign * res
