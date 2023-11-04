# Problem can be found here - https://leetcode.com/problems/permutation-in-string/description/

def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s2) < 2:
        return s1 == s2

    # Collect a dict of total number of char appearences in s1
    s1_map = {"total": 0}
    for char in s1:
        if char in s1_map.keys():
            s1_map[char] += 1
            s1_map["total"] += 1
        else:
            s1_map[char] = 1
            s1_map["total"] += 1
    total = s1_map["total"]

    l,r = 0,0
    while r < len(s2):
        char = s2[r]
        if char in s1_map.keys() and s1_map[char] != 0:
            s1_map[char] -=1
            total -=1
            r+=1
        elif s2[l] in s1_map.keys():
            total +=1
            s1_map[s2[l]] +=1
            l+=1
        else:
            l+=1;r+=1

        if total == 0:
            return True
    return False
