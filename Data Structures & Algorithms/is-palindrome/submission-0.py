class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ""
        for c in s:
            if c.isalnum():
                cleaned_str += c.lower()
        
        l = 0
        r = len(cleaned_str) - 1

        while l < r:
            if cleaned_str[l] != cleaned_str[r]:
                return False
            l += 1
            r -= 1

        return True