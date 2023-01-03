# https://leetcode.com/problems/maximum-number-of-balloons/description/

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict = {}
        arr = []
        for item in text:
            if item in 'balloon' and item not in dict:
                dict[item] = 1
            elif item in 'balloon' and item in dict:
                dict[item] += 1
        res = dict.get('z')
        if len(dict) < 5 or (dict['l'] < 2 and dict['o'] < 2):
            return 0
        for key in dict:
            if key == 'o' or key == 'l':
                arr.append(math.floor(dict[key] / 2))
            else:
                arr.append(dict[key])
        return min(arr)
