# https://leetcode.com/problems/candy/description/
def candy(self, ratings: List[int]) -> int:
    res = [1] * len(ratings)
    
    # right to left
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            res[i] = res[i - 1] + 1

    # left to right 
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i+1]:
            res[i] = max(res[i],res[i + 1] + 1)

    return sum(res)
