class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            res.append(self.getProduct(i,nums))
        return res

    def getProduct(self, idx: int, nums:List[int]) -> int:
        res = 1
        if idx == -1:
            return 0
        else:
            for i, num in enumerate(nums):
                if i != idx:
                    res *= num
            return res