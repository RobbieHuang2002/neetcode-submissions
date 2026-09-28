class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap, t_hashmap = {}, {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            s_hashmap[s[i]] = s_hashmap.get(s[i], 0) + 1
            t_hashmap[t[i]] = t_hashmap.get(t[i], 0) + 1
        
        if s_hashmap != t_hashmap:
            return False
        else: 
            return True
