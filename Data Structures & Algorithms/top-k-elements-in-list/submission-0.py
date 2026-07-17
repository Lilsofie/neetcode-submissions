class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       ans = [];
       data = [];
       total = 0;
       n = len(nums);
       for i in nums:
            if any(tup[1] == i for tup in data):
                continue;
            count = nums.count(i);
            tup = (count, i);
            data.append(tup);
            total += count;
            if total == n: break;
           
       sorted_data = sorted(data,key=lambda x: x[0]);

       m = len(sorted_data) - 1;
       print(sorted_data) 
       while k > 0:
           ans.append(sorted_data[m][1]) ;
           m = m - 1;
           k = k - 1;
       return ans;
    
       