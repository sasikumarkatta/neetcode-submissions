class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(numbers)):
            remain = target - numbers[i]
            if remain in dic :
                #if i+1 > dic[remain]:
                    #return [i+1,dic[remain]]
                
                return [dic[remain],i+1]

            else:
                dic[numbers[i]] = i+1


        