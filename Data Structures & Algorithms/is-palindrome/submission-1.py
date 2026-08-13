class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1: return True
        alphanum = "abcdefghijklmnopqsrtuvwxyz0123456789"
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and s[i] not in alphanum:
                i += 1
            while i < j and s[j] not in alphanum:
                j -= 1
            if i > j:
                break
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        