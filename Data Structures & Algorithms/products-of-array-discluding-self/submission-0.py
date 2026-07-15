class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list1 = []
        
        for i in range(len(nums)):
            val = 1
            for j in range(0,len(nums)):
                if i == j:
                    continue
                val = val * nums[j]
            
            list1.append(val)
        print(list1)
        return list1
        