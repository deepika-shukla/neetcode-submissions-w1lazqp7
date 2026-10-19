class Solution:
    def getRow(self, index: int) -> List[int]:
        if index == 0:
            return [1]
        if index == 1:
            return [1,1]
        
        prev = self.getRow(index - 1)
        cur = [1]
        for i in range(len(prev) - 1):
            cur.append(prev[i] + prev[i+1])
        cur.append(1)
        return cur
    