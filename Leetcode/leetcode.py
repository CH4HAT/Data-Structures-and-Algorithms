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