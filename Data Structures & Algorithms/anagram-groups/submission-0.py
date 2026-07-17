class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = [];
        check = {};
        for s in strs:
            chars = sorted(s);
            chars = ''.join(chars);
            if check.get(chars) == None:
                check[chars] = [s];
            else:
                check[chars].append(s);

        for chars in check:
            ans.append(check[chars]);

        return ans;

