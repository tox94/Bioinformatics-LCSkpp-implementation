from fenwick_tree import Fenwick_tree
from match_pairs import MatchPairs

def LCSkpp(k,string_1,string_2):
    #LCSkpp algorith implementation
    n=len(string_2)
    m=len(string_1)
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
        if event[2]==True: #if event is start
            value,parent=maxColDP.get(event[1])
            dp[event]=(k+value,parent) #O(log n) time
            continue_map[(event[0]+1,event[1]+1,event[2])]=event #create a map for every seen event
            #if the event is seen we create a i+1,j+1 bucket for it if i+1,j+1 exists we can find
            # its continuation in O(1) time
        else: #if event is end
            p=(event[0]-k,event[1]-k,True) #find substring start
            g=continue_map.get(p) #find the sequence it continues
            if g!=None:
                #update if continues and is greater than previous
                if dp[g][0]+1>dp[p][0]:
                    dp[p]=(dp[g][0]+1,g)
            #update the Fenwick tree with the longest match
            maxColDP.update(event[1],dp[p][0],p)

    #path reconstruction
    maximum_length=0
    child_first=(0,0,True)
    keys=[key for key in dp.keys()]
    keys.sort() #we sort the keys to find the biggest (row_major) index that has the maxValue
    for child in keys:
        value,p=dp[child]
        if value>=maximum_length:
            maximum_length=value
            child_first=child
    path=[(child_first[0],child_first[1])] #for the max value return the parent node
    child=child_first

    parent=(0,0,True)
    if maximum_length==0:
        return

    while(True):
        #walk through the parent child chain and remember the path
        v,parent=dp[child]
        if (parent==(-1,-1,True)):
            break
        #path.append((parent[0],parent[1]))
        path.append((parent[0],parent[1]))
        if (parent==(0,0,True)):
            break
        child=parent
    #reverse the path /we can also sort
    path.reverse()
    i_prev=j_prev=-k
    s1_m=s2_m=""
    test_s1=test_s2=""
    for step in path:
        i,j=step
        cri=chi=crj=chj=0
        #this is for - that indicate which characters we take from the sequence only for tests
        #not part of the final return
        if i-i_prev>=k:
            cri=i-i_prev-k
        else:
            chi=k-1
        if j-j_prev>=k:
            crj=j-j_prev-k
        else:
            chj=k-1

        s1_m+="-"*cri
        s2_m+="-"*crj
        #tests are the true sequences
        test_s1+=string_1[i+chi:i+k]
        test_s2+=string_2[j+chj:j+k]

        s1_m+=string_1[i+chi:i+k]
        s2_m+=string_2[j+chj:j+k]
        i_prev,j_prev=i,j

    s1_m+="-"*(m-len(s1_m))
    s2_m+="-"*(n-len(s2_m))
    f=open("py_output.txt","w")
    #f.write(string_1+"\n")
    #f.write(s1_m+"\n\n")

    #f.write(string_2+"\n")
    #f.write(s2_m+"\n\n")

    f.write(test_s1+"\n\n")
    #f.write(str(len(test_s1))+"\n\n")

    f.write(str(maximum_length)+"\n")

    return
