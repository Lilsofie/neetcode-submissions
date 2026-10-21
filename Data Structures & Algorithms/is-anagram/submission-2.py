class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        ts = sorted(t)
        if len(ss) != len(ts): return False
        for i in range(len(ss)):
            if ss[i] != ts[i]: return False
        return True