class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in dic:
                return [dic[rem],i]

            dic[num] = i
        
        print(dic)
