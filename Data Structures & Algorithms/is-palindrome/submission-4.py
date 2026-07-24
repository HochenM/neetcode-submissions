class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls =[]
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        
    
        for i in range(len(s) - 1, -1, -1):
            ls.append(s[i])

        reversed_str = "".join(ls)

        if reversed_str == s:
            return True
        else:
            return False