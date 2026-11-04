class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(char.lower() for char in s if char.isalnum())
        
        f, b = 0, len(cleaned_s) - 1
        
        while f < b:
            if cleaned_s[f] != cleaned_s[b]:
                return False
            f += 1
            b -= 1
            
        return True
