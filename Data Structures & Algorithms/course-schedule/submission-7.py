class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {}
        for i in range(numCourses):
            pre[i] = []
        
        for c, p in prerequisites:
            pre[c].append(p)

        visit = set()

        def dfs(crs):
            if pre[crs] == []:
                return True
            
            if crs in visit:
                return False # cycle
            
            visit.add(crs)
            for p in pre[crs]:
                if not dfs(p):
                    return False
            pre[crs] = []
            visit.remove(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True