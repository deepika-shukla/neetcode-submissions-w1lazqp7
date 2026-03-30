class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}
        for i in s1:
            hashmap[i] = 1 + hashmap.get(i,0)
        # print("h1",hashmap)
        
        hashmap2 = {}
        l = 0
        for i in range(len(s2)):
            hashmap2[s2[i]] =  1 + hashmap2.get(s2[i],0)
            if hashmap2 == hashmap:
                return True
            if (i-l+1) == len(s1):
                # print(hashmap2)
                if hashmap2[s2[l]] == 1:
                    del hashmap2[s2[l]]
                else:
                    hashmap2[s2[l]] -= 1
                l += 1
        return hashmap == hashmap2
