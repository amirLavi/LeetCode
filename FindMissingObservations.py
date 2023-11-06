# https://leetcode.com/problems/find-missing-observations/description/
def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
    mean_remainder = (mean * (len(rolls) + n)) - sum(rolls)
    res = []

    if mean_remainder < n or mean_remainder > n * 6:
        return []

    while mean_remainder:
        dice = min(mean_remainder - n + 1, 6)
        res.append(dice)
        n -=1
        mean_remainder -= dice
    return res
