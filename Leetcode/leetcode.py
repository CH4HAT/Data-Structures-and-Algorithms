# Climbing Stairs

class Solution:
    def step(self,n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.step(n-1)+ self.step(n-2)
    def climbStairs(self, n: int) -> int:
        return self.step(n)

# 0ms Runtime

class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 0
        for i in range(1, n+1):
            c = a + b
            b = a
            a = c
        return a 