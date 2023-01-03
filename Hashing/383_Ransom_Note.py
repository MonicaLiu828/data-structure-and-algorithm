class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = defaultdict(int)
        for item in magazine:
            dict[item]=dict.get(item,0)+1
        for item in ransomNote:
            if item not in dict:
                return False
            else:
                dict[item] -= 1
                if dict[item] < 0:
                    return False
        return True
    # n is length of magazine
    # Time: O(n)
    # space: O(n)