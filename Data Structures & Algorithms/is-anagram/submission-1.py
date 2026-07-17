class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        visited = []
        for c in s:
            if c not in visited:
                if s.count(c) != t.count(c):
                    return False
                visited.append(c);
        return True
        