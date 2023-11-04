# Problem can be found here - https://leetcode.com/problems/interleaving-string/description/
def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    if len(s3) != len(s1) + len(s2):
        return False
    inter_dic = {}

    def dfs(s1, s2, s3):
        if s3 == "":
            return True

        s1_bool, s2_bool = False, False
        
        if s1 != "" and s1[0] == s3[0]:
            if (s1,s3) in inter_dic.keys():
                s1_bool = inter_dic[(s1,s3)]
            else:
                s1_bool = dfs(s1[1:], s2, s3[1:])
                inter_dic[(s1,s3)] = s1_bool
        
        if s2 != "" and s2[0] == s3[0]:
            if (s2,s3) in inter_dic.keys():
                s2_bool = inter_dic[(s2,s3)]
            else:
                s2_bool = dfs(s1, s2[1:], s3[1:])
                inter_dic[(s2,s3)] = s2_bool
        
        return s1_bool or s2_bool
    

    return dfs(s1,s2,s3)
