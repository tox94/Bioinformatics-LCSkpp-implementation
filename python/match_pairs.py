from Math import *
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
    b=1
    while(i!=1):
        i>>=1
        b+=1
    return  b,characters

def r_hash(h,x,y,b,k):
    h-=(x<<(k*b))
    h<<=b
    h+=y
    return h

def MatchPairs(string_1,string_2,k):
    b,characters=setup_characters(string_1,string_2)

    table={}

    h=r_hash(0,0,characters[string_1[0]],b,k)
    for i in range(1,k):
        h=r_hash(h,0,characters[string_1[i]],b,k)
    table[h].append(0)
    for i in range(k,len(string))
        h=r_hash(h,characters[string_1[i-k]],characters[string_1[i]],b,k)
        table[h].append(i)

    pairs=[]
    h=r_hash(0,0,characters[string_2[0]],b,k)
    for i in range(1,k):
        h=r_hash(h,0,characters[string_2[i]],b,k)
    pairs.extend([(i,k,0) for i in table[h]]
    for j in range(k,len(string))
        h=r_hash(h,characters[string_2[j-k]],characters[string_2[j]],b,k)
        pairs.extend([(i,j,0) for i in table[h]])

    pairs_e=[(i+k,j+k,1) for i,j,_ in pairs]
    pairs.extend(pairs_e)
    r=len(pairs)
    pairs.sort(key=lambda x: (x[0]+1)*len(string_1)*len(string_2)+(x[1]+1)*len(string_2)+x[2])
    return pairs
