class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)
        result = []

        while k != 0:
            maxKey = max(countMap, key=countMap.get)
            countMap.pop(maxKey)
            result.append(maxKey)
            k -= 1
        return result
        