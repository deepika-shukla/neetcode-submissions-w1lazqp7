class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # first we will create an adjancency list
        adj = {i : [] for i in range(numCourses)}
        for c1,c2 in prerequisites:
            adj[c1].append(c2)

        visit = set()

        # now create our dfs function
        def dfs(crs):
        # if that crs is visited tehn we detected a loop
            if crs in visit:
                return False
            
            # if no prereq then True
            if adj[crs] == []:
                return True
            visit.add(crs)
            # now check for neighbours
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
                
            
            # now remove from visit set once course is completed
            visit.remove(crs)
            adj[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        

                