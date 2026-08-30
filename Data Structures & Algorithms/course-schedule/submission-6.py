class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # first we creat an adjancency list
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        print(adj)
        
        cycle = set()
        visit = set()

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            if adj[crs] == []:
                return True
            
            cycle.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)
            adj[crs] = []
            visit.add(crs)
            return True

            

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True