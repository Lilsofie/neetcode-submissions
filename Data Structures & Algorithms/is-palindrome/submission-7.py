class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = "".join(c.lower() for c in s if c.isalnum())
        print(newStr)
        return newStr==newStr[::-1]