def setup_characters(x,y):
    characters={}
    i=0
    for x_c in x:
        if x_c not in characters:
            characters[x_c]=i
            i+=1
    for y_c in y:
        if y_c not in characters:
            characters[y_c]=i
            i+=1
    i-=1
    b=1
    while(i!=1):
        i>>=1
        b+=1

    return  b,characters

def r_hash(h,y,b,k,mask):
    h<<=b
    h+=y
    h&=mask
    return h

def MatchPairs(string_1,string_2,k):
    b,characters=setup_characters(string_1,string_2)
    pairs=[]
    table={}
    mask=2**(b*k)-1
    #print (b,k)
    #print (mask)
    h=r_hash(0,characters[string_1[0]],b,k,mask)

    for i in range(1,k):
        h=r_hash(h,characters[string_1[i]],b,k,mask)
    if h not in table:
        table[h]=[]
    table[h].append(0)
    for i in range(k,len(string_1)):
        h=r_hash(h,characters[string_1[i]],b,k,mask)
        if h not in table:
            table[h]=[]
        table[h].append(i-k+1)
    h=0
    h=r_hash(0,characters[string_2[0]],b,k,mask)
    for i in range(1,k):
        h=r_hash(h,characters[string_2[i]],b,k,mask)
    if h in table:
        pairs.extend([(i,0,False) for i in table[h]])
    for j in range(k,len(string_2)):
        h=r_hash(h,characters[string_2[j]],b,k,mask)
        if h not in table:
            continue
        pairs.extend([(i,j-k+1,False) for i in table[h]])

    #print (table.keys(),len(table))
    #print (characters)

    pairs_e=[(i+k,j+k,True) for i,j,_ in pairs]
    pairs.extend(pairs_e)
    r=len(pairs)
    pairs.sort()
    return pairs
