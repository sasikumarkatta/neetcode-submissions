class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        low = 0
        high = len(s)-1
        while low <=high:
            if not s[low].isalnum() or not s[high].isalnum():
                if not s[low].isalpha():
                    low +=1
                if not s[high].isalpha():
                    high-=1
                continue

            if s[low].lower() == s[high].lower():
                print(s[low],s[high])
                low+=1
                high-=1
            
            else:
                return False
        return True
        