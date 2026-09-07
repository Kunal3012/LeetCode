class Solution(object):
    def climbStairs(self, n):
        def multiply(a, b):
            return [
                [a[0][0]*b[0][0] + a[0][1]*b[1][0],
                 a[0][0]*b[0][1] + a[0][1]*b[1][1]],
                [a[1][0]*b[0][0] + a[1][1]*b[1][0],
                 a[1][0]*b[0][1] + a[1][1]*b[1][1]]
            ]
        
        def matrix_pow(mat, power):
            result = [[1, 0], [0, 1]]  # Identity matrix
            while power > 0:
                if power % 2 == 1:
                    result = multiply(result, mat)
                mat = multiply(mat, mat)
                power //= 2
            return result
        
        if n <= 2:
            return n
        
        base = [[1, 1], [1, 0]]
        result = matrix_pow(base, n - 2)
        return result[0][0]*2 + result[0][1]*1