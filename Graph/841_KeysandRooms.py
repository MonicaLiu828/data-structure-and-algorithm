class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # stor = defaultdict(list)
        seen = set()
        seen.add(0)
        totalroom = len(rooms)

        # for i in range(totalroom):
        #     for item in rooms[i]:
        #         stor[i].append(item)
        # {0:[1,3]}
        def dfs(room):
            for item in rooms[room]:
                if item not in seen:
                    seen.add(item)
                    dfs(item)
            return

        dfs(0)
        # for key in stor:
        #     if key not in seen:
        #         return False

        return totalroom == len(seen)

        # time: O(n+e) n is the number of rooms and e is number of keys(e may have repetitive room numbers, for Example 2: key is 1,3,3,0,1,2,0)
        # space: O(n) n since extra space is number of rooms 
