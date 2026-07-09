class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
    # Step 2: Create buckets where the index represents the frequency
    # We need len(nums) + 1 buckets to safely handle an index equal to len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
    
        for num, freq in count.items():
            buckets[freq].append(num)
        
    # Step 3: Collect the top k elements by iterating backwards through buckets
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
            # Break immediately when we've gathered k elements
                if len(result) == k:
                    return result

        