from fenwick_tree import Fenwick_tree
from match_pairs import MatchPairs

def LCSkpp(k,string_1,string_2):
    #LCSkpp algorith implementation
    maxColDP=Fenwick_tree(len(string_2))
    #maxColDP is a Fenwick tree for fas calculation of maxRange query in the range of [0,j]
    events,r=MatchPairs(string_1,string_2,k)
    #events is a sorted list of all the substring pair starts and ends in row major ordering
    dp={}
    #dp is a map of sunsequence values per event start len(dp)=r(number of Match Pairs)
    continue_map={}
    #continue map every start that exists is stored on the (i+1,j+1) place so if (i+1,j+1)
    # exists we can get the sequence it continues in O(log n) time
    for event in events:
        if event[2]==0:
            dp[event]=0
            continue_map[(event[0]+1,event[1]+1,event[2])]=event

    for event in events:
        if event[2]==0: #if event is start
            dp[event]=k+maxColDP.get(event[1]) #O(log n) time
        else: #if event is end
            p=(event[0]-k,event[1]-k,0) #find event start
            g=continue_map.get(p) #find tje sequence it continues
            if g!=None:
                #update if continues
                dp[p]=max(dp[p],dp[g]+1)
            #update the Fenwick tree with the longest match
            maxColDP.update(event[1],dp[p])
    return max(dp.values())
