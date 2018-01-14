from fenwick_tree import Fenwick_tree
from match_pairs import MatchPairs

def continues(x,events):
    g=[]
    ipjp=x[0]-x[1]
    for y in events:
        if x==y:
            break
        if y[2]==1:
            continue
        if (ipjp==y[0]-y[1]) and (x[0]-y[0]==1):
            g.append(y)
    return g


def LCSkpp(k,string_1,string_2):
    maxColDP=Fenwick_tree(len(string_2))
    events=MatchPairs(string_1,string_2,k)
    print (events)
    dp={}
    i=0
    for event in events:
        if event[2]==0:
            dp[event]=0
    for event in events:
        if event[0]!=i:
            i=event[0]
            print (i)
        if event[2]==0:
            dp[event]=k+maxColDP.get(event[1])
        else:
            p=(event[0]-k,event[1]-k,0)
            g_list=continues(p,events)
            for g in g_list:
                dp[p]=max(dp[p],dp[g]+1)
            maxColDP.update(event[1],dp[p])
        #print(maxColDP.get(len(string_2)))
    m=0
    print ("kaos")
    for event in events:
        if event[2]==0:
            pom=dp[event]
            if pom>m:
                m=pom
    return m
