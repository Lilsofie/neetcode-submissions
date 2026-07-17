class Solution:
    def climbStairs(self, n: int) -> int:
        to_curr, to_prev = 1,1
        
        for i in range(n-1):
            temp  = to_curr
            to_curr = to_curr + to_prev
            to_prev = temp
        
        return to_curr