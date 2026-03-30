class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            count = 0
            for i in word:
                if i == "a":
                    count += 29
                else:    
                    count += (ord(i) - ord('a'))
            print(count)
            if count not in d:
                d[count] = [word]
            else:
                d[count].append(word)
        return d.values()