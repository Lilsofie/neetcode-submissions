class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = self.getChar(s);
        t_char = self.getChar(t);
        if s_char == t_char :
            return True;
        return False;

    def getChar(self, s:str) -> dict:
        result = {};
        for i in s:
            if result.get(i)== None:
                result[i] = 1;
            else:
                k = result[i];
                k += 1;
                result[i] = k;
        return result;