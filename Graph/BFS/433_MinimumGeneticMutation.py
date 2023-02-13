class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankSet = set(bank)
        queue = deque()
        queue.append([startGene, 0])
        seen = set()
        seen.add(startGene)
        res = -1
        # def bfs():
        while queue:
            node, step1 = queue.popleft()
            if node == endGene:
                res = step1
                return res
            for item in 'ACGT':
                for j in range(8):
                    newGene = node[:j] + item + node[j + 1:]
                    if newGene in bankSet and \
                            newGene not in seen:
                        seen.add(newGene)
                        queue.append([newGene, step1 + 1])
        # bfs()
        if res == -1:
            return res
