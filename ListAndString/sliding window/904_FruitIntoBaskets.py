class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window
        stor = defaultdict(int)
        maxCount = 0
        count = 0
        i, j, k = [0, 0, 0]

        while j < len(fruits):
            if fruits[j] not in stor:
                k += 1
            stor[fruits[j]] += 1
            count += 1
            if k <= 2:
                # don't forget to get max with each step, else in [1,2,3,3,4] you will
                # not get correct answer
                maxCount = max(maxCount, count)
            if k > 2:
                while i <= j:
                    curr = fruits[i]
                    stor[curr] -= 1
                    count -= 1
                    # don't forget to add i one step since you will get -1 as value
                    # of map of key
                    i += 1
                    if stor[curr] == 0:
                        # don't forget to delete this key when it becomes to 0
                        del stor[curr]
                        k -= 1
                        maxCount = max(maxCount, count)
                        break
            j += 1
        return maxCount

# Time complexity: O(n)O(n)O(n)

# Similarly, both indexes left and right are only monotonically increasing during the iteration, thus we have at most 2⋅n2 \cdot n2⋅n steps,
# At each step, we update the hash set by addition or deletion of one fruit, which takes constant time. Note that the number of additions or deletions does not exceed nnn.
# To sum up, the overall time complexity is O(n)O(n)O(n)
# Space complexity: O(1)O(1)O(1)

# We maintain the number of fruit types contained in the window in time. Therefore, at any given time, there are at most 3 types of fruits in the window or the hash map basket.
# In summary, the space complexity is O(1)O(1)O(1).

