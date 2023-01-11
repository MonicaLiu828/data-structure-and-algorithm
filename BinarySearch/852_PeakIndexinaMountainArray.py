class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # convert arr[0,1,0] into true, true,false [0, 1-0, 0-1](use arr[i+1]-arr[i] find if it's > 0, give it as true)
        # you need to find the last true index (is the same as arr find right most index where the value === target)
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            # if at the mid point it's is true, move left to this middle point
            if arr[mid] - arr[mid - 1] > 0:
                left = mid
            else:
                right = mid - 1
        return left

