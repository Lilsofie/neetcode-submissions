class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in idMap:
                return [idMap[diff], i]
            idMap[n] = i