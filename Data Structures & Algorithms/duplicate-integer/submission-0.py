class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         ans = {};
         for i in nums:
            if ans.get(i)!= None :
                return True;
            ans[i] = 1;   
         return False;
         
        