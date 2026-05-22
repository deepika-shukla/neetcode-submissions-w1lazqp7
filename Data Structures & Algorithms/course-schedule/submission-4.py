class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visit = set()

        def dfs(crs):
            # if course in visit, loop
            if crs in visit:
                return False
            
            # check if no prerequisite
            if adj[crs] == []:
                return True # can be completed
            
            visit.add(crs)
            for nei in adj[crs]:
                # if we are not able to complete even 1 return False
                if not dfs(nei):
                    return False
            
            # for bactrack remove course
            visit.remove(crs)
            adj[crs] = []
            return True
        
        # check for every course
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True