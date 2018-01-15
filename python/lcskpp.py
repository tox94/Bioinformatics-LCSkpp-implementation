from fenwick_tree import Fenwick_tree
from match_pairs import MatchPairs

def LCSkpp(k,string_1,string_2):
    #LCSkpp algorith implementation
    n=len(string_2)
    maxColDP=Fenwick_tree(n)
    #maxColDP is a Fenwick tree for fas calculation of maxRange query in the range of [0,j]
    events,r=MatchPairs(string_1,string_2,k)
    #events is a sorted list of all the substring pair starts and ends in row major ordering
    dp={}
    #dp is a map of sunsequence values per event start len(dp)=r(number of Match Pairs)
    continue_map={}
    #continue map every start that exists is stored on the (i+1,j+1) place so if (i+1,j+1)
    # exists we can get the sequence it continues in O(log n) time
    for event in events:
        if event[2]==False:
            dp[event]=0
            continue_map[(event[0]+1,event[1]+1,event[2])]=event

    for event in events:
        if event[2]==False: #if event is start
            value,parent=maxColDP.get(event[1])
            dp[event]=(k+value,parent) #O(log n) time
        else: #if event is end
            p=(event[0]-k,event[1]-k,False) #find event start
            g=continue_map.get(p) #find the sequence it continues
            if g!=None:
                #update if continues
                dp[p]=(dp[g][0]+1,g)
            #update the Fenwick tree with the longest match
            maxColDP.update(event[1],dp[p][0],p)

    #path reconstruction
    maximum_length=0
    child_first=(0,0,False)
    for child in dp.keys():
        value,p=dp[child]
        if value>maximum_length:
            maximum_length=value
            child_first=child
    path=[(child_first[0],child_first[1])]
    child=child_first
    print (child_first)
    parent=(0,0,False)
    while(True):
        v,parent=dp[child]
        if (parent==(-1,-1,False)):
            break
        #path.append((parent[0],parent[1]))
        if (parent==(0,0,False)):
            break
        path.append((parent[0],parent[1]))

        child=parent
    path.reverse()
    i_prev=j_prev=-k
    s1_m=s2_m=""
    for step in path:
        i,j=step
        s1_m+="-"*(i-i_prev-k)
        s2_m+="-"*(j-j_prev-k)
        s1_m+=string_1[i-max(0,-(i-i_prev-k)):i+k]
        s2_m+=string_2[j-max(0,-(j-j_prev-k)):j+k]
        i_prev,j_prev=i,j
    s1_m+="-"*(len(string_1)-len(s1_m))
    s2_m+="-"*(len(string_2)-len(s2_m))
    print (string_1)
    print (s1_m)
    print ("\n")
    print (string_2)
    print (s2_m)
    print ("\n")
    return maximum_length
