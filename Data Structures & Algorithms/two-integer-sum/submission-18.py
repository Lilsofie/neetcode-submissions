class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement = target - nums[i];
            if nums.count(complement) > 0:
                e = nums.index(complement);
                if(e == i):
                    temp  = nums[i + 1:];
                    print(temp);
                    if complement in temp:
                        e = temp.index(complement) + i + 1; 
                    else:
                        continue;
                return [i, e];
