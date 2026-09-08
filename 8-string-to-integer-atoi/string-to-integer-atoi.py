class Solution:
    def myAtoi(self, s: str) -> int:
        # Removing leading whitespace
        s = s.lstrip()
        
        if not s:
            return 0  # If the string is empty after removing whitespace
        
        sign = 1  # Initialize sign as positive by default
        result = 0
        i = 0
        
        # Check for sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        # Applying sign and clamping the result to 32-bit signed integer range
        result *= sign
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result