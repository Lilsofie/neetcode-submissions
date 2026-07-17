class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            hveyest = stones.pop(-1)
            hvey = stones.pop(-1)
            if hveyest > hvey:
                diff = hveyest - hvey 
                stones.append(diff)
        if len(stones) >= 1:
            return stones[0]
        return 0