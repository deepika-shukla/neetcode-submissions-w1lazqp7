class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # we will first create adjacency list
        adj = {c : [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        # visit, cycle
        visit, cycle= set(), set()
        output= []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                # this course can be cleared
                return True
            
            cycle.add(crs)
            # check for neighbour
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            
            visit.add(crs)
            cycle.remove(crs)
            output.append(crs)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output