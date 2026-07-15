class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        #return nums + nums
        n = len(nums)
        ans = nums + [0]*n
        for i in range(n):
            ans[i+n] = nums[i]
        
        return ans


        