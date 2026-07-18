class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ""
        # if not strs:
        #     return []
        for s in strs:
            encode_string +=str(len(s)) + "#" + s
        return encode_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        # if not s:
        #     return []
        while i < len(s):

            j = i

            while s[j] != "#":
                 j+=1
        
            le = int(s[i:j])
            i = j+1
            result.append(s[i:i+le])
            i = i+le


        return result
            
