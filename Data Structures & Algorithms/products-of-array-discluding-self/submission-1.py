class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list1 = []
        n = len(nums)
        final = [1]*n
        prefix = 1
        for i in range(n):
            final[i]= final[i] * prefix
            prefix = prefix * nums[i]
        
        suffix = 1
        for i in range(n-1,-1,-1):
            final[i] = final[i] * suffix
            suffix = suffix * nums[i]
        
        return final
        
        # for i in range(len(nums)):
        #     val = 1
        #     for j in range(0,len(nums)):
        #         if i == j:
        #             continue
        #         val = val * nums[j]
            
        #     list1.append(val)
        # print(list1)
        # return list1
        
        