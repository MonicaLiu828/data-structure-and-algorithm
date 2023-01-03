# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated
# player loseri in a match.
#
# Return a list answer of size 2 where:
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.
#
# Note:
# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict1 = {}
        dict2 = {}
        winner = []
        loser = []
        for item in matches:
            if item[0] not in dict1:
                dict1[item[0]] = 1
            else:
                dict1[item[0]] += 1
            if item[1] not in dict2:
                dict2[item[1]] = 1
            else:
                dict2[item[1]] += 1
        for key in dict1:
            if key not in dict2:
                winner.append(key)
        for key in dict2:
            if dict2[key] == 1:
                loser.append(key)
        final = []
        winner.sort()
        loser.sort()
        final.append(winner)
        final.append(loser)
        return final