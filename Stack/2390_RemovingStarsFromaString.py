class Solution:
    def removeStars(self, s: str) -> str:
        stor = []
        for item in s:
            if item != '*':
                stor.append(item)
            if item == "*":
                stor.pop()
        return ''.join(stor)