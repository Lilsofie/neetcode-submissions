class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c = matrix
        for i in range(len(c)):
            m = max(c[i])
            if target > m:
                continue;
            elif target < m:
                return target in c[i]
            else:
                 return True
        return False