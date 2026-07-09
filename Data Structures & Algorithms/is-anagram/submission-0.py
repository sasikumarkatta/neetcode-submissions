class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        i = 0
        dic = {}
        while i<=(len(s)-1):
            if s[i] in dic :
                dic[s[i]] +=1
                i +=1
            
            else:
                dic[s[i]] = 1
                i +=1
        
        j = 0
        while j<=(len(t)-1):
            if t[j] in dic:
                dic[t[j]] -= 1
                
                if dic.get(t[j]) == 0:
                    dic.pop(t[j])

                j += 1
                
            else:
                print("false")
                return False
        
        return True



