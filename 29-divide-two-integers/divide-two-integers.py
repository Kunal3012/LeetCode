class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        if dividend == 0:
            return 0
        if divisor == 1:
            return min(MAX_INT, max(MIN_INT, dividend))
        if divisor == -1:
            return min(MAX_INT, max(MIN_INT, -dividend))
        
        negative = (dividend < 0) ^ (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            power = 0
            while dividend >= (divisor << power):
                power += 1
            quotient += 1 << (power - 1)
            dividend -= divisor << (power - 1)
        
        if negative:
            quotient = -quotient
        
        return min(MAX_INT, max(MIN_INT, quotient))