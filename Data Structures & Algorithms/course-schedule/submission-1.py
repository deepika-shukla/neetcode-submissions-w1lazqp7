class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we can find loop meaning cocurse will not complete

        adj = {i:[] for i in range(numCourses)}

        visit = set()

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        def dfs(crs):
            if crs in visit:
                return False
            
            if adj[crs] == []:
                return True
            
            visit.add(crs)

            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            
            visit.remove(crs)
            adj[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                 return False
        return True
