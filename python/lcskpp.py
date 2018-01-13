from fenwick_tree import Fenwick_tree
from match_pairs import MatchPairs

def LCSk++(k.string_1,string_2):
    maxColDP=Fenwick_tree(len(string_1))
    events=match_pairs(string_1,string_2,k)
    dp={}

    for event in events:
        if event[2]==0:
            dp[event]=k+maxColDP.get[event[1]]
        else:
            flag,g=continues(event,events)
            for i in range(flag):
                dp[event]=max(dp[event],dp[g[i]]+1)
            maxColDP.update(event[2],dp[event]
    return max(dp)
