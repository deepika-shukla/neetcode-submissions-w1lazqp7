class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        
        for pre, crs in prerequisites:
            adj[crs].append(pre)
    

        def dfs(crs):
            if crs not in premap:
                premap[crs] = set()
                for prereq in adj[crs]:
                    # union the set of all prereq as well
                    premap[crs] |= dfs(prereq)
                # add the course as well
                premap[crs].add(crs)
            
            return premap[crs] # it will return hashset
        
        premap = {} # crs -> set of prerequisites
        res = []
        for crs in range(numCourses):
            dfs(crs)

        for u,v in queries:
            if u in premap[v]:
                res.append(True)
            else:
                res.append(False)
        return res