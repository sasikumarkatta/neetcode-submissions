class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        g = (len(s)-1)
        i = 0
        dic = {}
        while i<=g:
            if s[i] in dic :
                dic[s[i]] +=1
                i +=1
            
            else:
                dic[s[i]] = 1
                i +=1
        
        i = 0
        while i<=g:
            if t[i] in dic:
                dic[t[i]] -= 1
                
                if dic.get(t[i]) == 0:
                    dic.pop(t[i])

                i += 1
                
            else:
                return False
        
        return True



