class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guards_set = {tuple(g) for g in guards}
        walls_set = {tuple(w) for w in walls}
        gaurded = set()

        # up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for gx, gy in guards_set:
            for dx, dy in directions:
                x, y = gx + dx, gy + dy

                while 0 <= x < m and 0 <= y < n and (x, y) not in walls_set and (x,y) not in guards_set:
                    gaurded.add((x,y))
                    x += dx
                    y += dy

        # Total Area - total area covered by walls - total area covered by gaurds
        total_empty = m * n - len(walls_set) - len(guards_set)

        return total_empty - len(gaurded)
