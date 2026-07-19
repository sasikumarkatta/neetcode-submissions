class Solution:
    def maxArea(self, heights: List[int]) -> int:

        low = 0
        high = len(heights)-1
        max_water = 0
        current = heights[high]
        while low <high:
            if heights[high]<current:
                high-=1
                continue
            diff = high-low
            current_height = min(heights[low],heights[high])
            current_water = current_height*diff
            if current_water > max_water :
                max_water = current_water
                current = heights[high]
            #max_water = max(max_water,current_height*diff)
            if heights[low] < heights[high]:
                low +=1
            
            else:
                high-=1
            
        return max_water
        