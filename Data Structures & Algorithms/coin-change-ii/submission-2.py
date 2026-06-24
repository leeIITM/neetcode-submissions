class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # solving using memoization
        d ={}
        def pick_not_pick(i, leftout):
            if leftout == 0:
                return 1
            if leftout <0 or i == len(coins):
                return 0
            # if pick
            if ((i,leftout - coins[i]) not in d):
                pick = pick_not_pick(i, leftout-coins[i])
                d[(i,leftout - coins[i])] = pick
            else:
                pick = d[(i,leftout - coins[i])]
            # if not pick
            if ((i,leftout) not in d):
                not_pick = pick_not_pick(i+1, leftout)
                d[(i+1,leftout)] = not_pick
            else:
                not_pick = d[(i+1,leftout)]
            
            

            return pick + not_pick
        
        return pick_not_pick(0,amount)
    