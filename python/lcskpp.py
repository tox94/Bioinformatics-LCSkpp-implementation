from fenwick_tree import Fenwick_tree
from match_pairs import MatchPairs

def LCSkpp(k,string_1,string_2):
    maxColDP=Fenwick_tree(len(string_2))
    events=MatchPairs(string_1,string_2,k)
    dp={}
    i=0
    continue_map={}
    for event in events:
        if event[2]==0:
            dp[event]=0
            continue_map[(event[0]+1,event[1]+1,event[2])]=event
    for event in events:
        if event[2]==0:
            dp[event]=k+maxColDP.get(event[1])
        else:
            p=(event[0]-k,event[1]-k,0)
            g=continue_map.get(p)
            if g!=None:
                dp[p]=max(dp[p],dp[g]+1)
            maxColDP.update(event[1],dp[p])
        #print(maxColDP.get(len(string_2)))
    return max(dp.values())
