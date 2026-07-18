class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        long_state = 0
        for num in nums:

            if num-1 not in nums:
                current_num = num
                current_state = 1

                while current_num+1 in nums:
                    current_num+=1
                    current_state +=1

                long_state = max(long_state,current_state)
        
        return long_state

        