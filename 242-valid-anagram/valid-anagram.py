class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        count = {}
        
        # Build frequency map using s and subtract using t
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
            
        # If any character frequency is not zero, return False
        for val in count.values():
            if val != 0:
                return False
                
        return True
