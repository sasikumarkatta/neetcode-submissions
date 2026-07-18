class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        list1 = []
        for i in range(len(nums)-2):
            if nums[i]>0 and nums[i+1]!=0:
                return list1
    
            low = i+1
            high = len(nums)-1
            
            while low < high:
                if nums[i]+nums[low]+nums[high] == 0:
                    if [nums[i],nums[low],nums[high]] not in list1:
                        list1.append([nums[i],nums[low],nums[high]])
                    
                    low+=1
                    high -=1

                elif nums[i]+nums[low]+nums[high] > 0:
                    high -=1
                
                else:
                    low+=1
        return list1
        