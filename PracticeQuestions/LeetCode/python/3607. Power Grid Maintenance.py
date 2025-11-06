from collections import defaultdict
from bisect import insort, bisect_left

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DSU(c)
        from collections import defaultdict
from bisect import bisect_left

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # ---------- DSU IMPLEMENTATION ----------
        parent = list(range(c + 1))
        rank = [0] * (c + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            xr, yr = find(x), find(y)
            if xr == yr:
                return
            if rank[xr] < rank[yr]:
                parent[xr] = yr
            elif rank[xr] > rank[yr]:
                parent[yr] = xr
            else:
                parent[yr] = xr
                rank[xr] += 1

        # ---------- BUILD COMPONENTS ----------
        for u, v in connections:
            union(u, v)

        comp_members = defaultdict(list)
        for i in range(1, c + 1):
            comp_members[find(i)].append(i)

        # Maintain sorted list of online stations per component
        comp_online = {root: sorted(members) for root, members in comp_members.items()}
        online = [True] * (c + 1)

        # ---------- PROCESS QUERIES ----------
        res = []

        for qtype, x in queries:
            if qtype == 1:
                # Maintenance check
                if online[x]:
                    res.append(x)
                else:
                    root = find(x)
                    arr = comp_online[root]
                    res.append(arr[0] if arr else -1)

            elif qtype == 2:
                # Station goes offline
                if not online[x]:
                    continue
                online[x] = False
                root = find(x)
                arr = comp_online[root]
                idx = bisect_left(arr, x)
                if idx < len(arr) and arr[idx] == x:
                    arr.pop(idx)

        return res

        for u, v in connections:
            dsu.union(u, v)
        
        comp_members = defaultdict(list)
        for i in range(1, c+1):
            comp_members[dsu.find(i)].append(i)
        
        # Each component maintains a sorted list of online stations
        comp_online = {root: sorted(members) for root, members in comp_members.items()}
        online = [True] * (c + 1)
        
        res = []
        
        for qtype, x in queries:
            if qtype == 1:
                if online[x]:
                    res.append(x)
                else:
                    root = dsu.find(x)
                    arr = comp_online[root]
                    res.append(arr[0] if arr else -1)
            
            elif qtype == 2:
                if not online[x]:
                    continue
                online[x] = False
                root = dsu.find(x)
                arr = comp_online[root]
                idx = bisect_left(arr, x)
                if idx < len(arr) and arr[idx] == x:
                    arr.pop(idx)
        
        return res
