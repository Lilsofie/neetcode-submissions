class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            l = target - nums[i]
            if l in nums:
                idx = nums.index(l)
                if idx != i:
                    return [min(i, idx), max(i,idx)]
