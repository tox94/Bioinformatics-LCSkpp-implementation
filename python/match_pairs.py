def setup_characters(x,y):
    #setup characters finds all the unique characters in the strings and calculates their codes
    #also returns the size of code
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
    #rolling_hash function removes the oldest character code and appends the new code
    h<<=b
    h+=y
    h&=mask
    return h

def MatchPairs(string_1,string_2,k):
    #MatchPairs function calculates all the k substring paris between 2 strings
    b,characters=setup_characters(string_1,string_2)
    #b=bits per character code, characters dictionary character->code
    pairs=[]
    table={}
    #mask is the size of a codeword
    # example: for 3 bits per code and 3 characters in codeword
    # we need 3*3=9 bits 2*9-1=511 = 00111111111(2)
    mask=2**(b*k)-1

    #calculate the hash for the first k characters
    h=r_hash(0,characters[string_1[0]],b,k,mask)
    for i in range(1,k):
        h=r_hash(h,characters[string_1[i]],b,k,mask)
    if h not in table:
        table[h]=[]
    for i in range(k,len(string_1)):
        #for every new character update the hash
        h=r_hash(h,characters[string_1[i]],b,k,mask)
        if h not in table:
            table[h]=[]
        table[h].append(i-k+1)

    #calculate the hash for the first k characters
    h=r_hash(0,characters[string_2[0]],b,k,mask)
    for i in range(1,k):
        h=r_hash(h,characters[string_2[i]],b,k,mask)
    if h in table:
        pairs.extend([(i,0,False) for i in table[h]])
    for j in range(k,len(string_2)):
        #for every new character update the hash
        h=r_hash(h,characters[string_2[j]],b,k,mask)
        if h not in table:
            continue
        pairs.extend([(i,j-k+1,False) for i in table[h]])
    r=len(pairs)
    pairs_e=[(i+k,j+k,True) for i,j,_ in pairs]
    pairs.extend(pairs_e)
    pairs.sort()

    return pairs,r
