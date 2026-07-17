class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        for word in strs:
            s = sorted(word)
            flag = 0
            for item in result:
                i = sorted(item[0])
                if i == s:
                    item.append(word)
                    flag = 1
                    break;
            if flag == 0:
                result.append([word])
                
        return result