class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        mp = defaultdict(int)

        for x in bills:
            if x == 20:
                if mp[10]>=1 and mp[5]>=1:
                    mp[10] -= 1
                    mp[5] -= 1
                elif mp[5]>=3:
                    mp[5] -= 3
                else:
                    return False
            elif x == 10:
                if mp[5]>=1:
                    mp[5] -= 1
                else:
                    return False
            mp[x] += 1
        return True