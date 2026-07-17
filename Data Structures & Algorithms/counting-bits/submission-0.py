class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            s = bin(i)
            count = s.count('1')
            res.append(count)
        return res
