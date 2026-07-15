class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if len(nums) == len(set(nums)) :
        #     return False
        
        # else :
        #     return True
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic :
                return True
            else:
                dic[nums[i]] = 1
        
        return False