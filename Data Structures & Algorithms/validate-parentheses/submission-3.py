class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(':')','{':'}','[':']'}
        for ch in s:
            if ch in mapping:
                stack.insert(0, mapping[ch])
            else:
                print(stack)
                if len(stack) == 0:
                    return False
                if ch == stack[0]:
                    stack.pop(0)
                else:return False
        return len(stack) == 0
        