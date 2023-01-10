class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # sort potions
        # if middle of sort * spell >= success, move r to middle(find the first number * spell >= target)
        res = []
        potions.sort()

        for item in spells:
            l = 0
            r = len(potions)
            while l < r:
                m = (l + r) // 2
                if item * potions[m] >= success:
                    r = m
                else:
                    l = m + 1
            num = len(potions) - l
            res.append(num)
        return res

# time:(m+n)logm -> m stands for pitions length, n stands for spells length
# space: O1


//given standard answer:
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(arr, target):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        potions.sort()
        ans = []
        m = len(potions)

        for spell in spells:
            i = binary_search(potions, success / spell)
            ans.append(m - i)

        return ans