class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        seen = set()
        seen.add((entrance[0], entrance[1]))
        stor = deque()
        stor.append([entrance[0], entrance[1], 0])
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        row = len(maze)
        col = len(maze[0])
        minStep = float('inf')

        while stor:
            r, c, s = stor.popleft()
            for item in direction:
                newr = r + item[0]
                newc = c + item[1]
                news = s + 1

                if 0 <= newr <= row - 1 and 0 <= newc <= col - 1 and maze[newr][newc] == '.':
                    if (newr, newc) not in seen:
                        if newr == 0 or newc == 0 or newc == col - 1 or newr == row - 1:
                            seen.add((newr, newc))
                            minStep = min(minStep, news)
                            continue
                        stor.append([newr, newc, news])

                # if newr >=0 and newr <= row -1 and newc >= 0 and newc <= col -1:
                #     if (newr,newc) in seen or maze[newr][newc] == '+':
                #         continue
                # if newr < 0 or newr > row-1 or newc < 0 or newc > col-1:
                #     continue
                # if newr == 0 or newc == 0 or newc == col-1 or newr == row-1:
                #     seen.add((newr,newc))
                #     minStep = min(minStep,news)
                #     continue
                # seen.add((newr,newc))
                # stor.append([newr,newc,news])

        if minStep == float('inf'):
            return -1
        else:
            return minStep