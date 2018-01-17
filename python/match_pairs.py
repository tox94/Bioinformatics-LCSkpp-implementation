def setup_characters(x,y):
    #setup characters finds all the unique characters in the strings and calculates their codes
    #also returns the size of code b
    characters={}
    #dictionary for charcter codes
    i=0
    for x_c in x:
        if x_c not in characters: #if character not seen add its code
            characters[x_c]=i
            i+=1
    for y_c in y:
        if y_c not in characters: #if character not seen add its code
            characters[y_c]=i
            i+=1
    i-=1
    b=1
    while(i!=1):
        i>>=1
        b+=1
        #calculate the number of bits required for the codes
    return  b,characters

def r_hash(h,y,b,k,mask):
    #rolling_hash function removes the oldest character code and appends the new code
    h<<=b #shift left one chracter code
    h+=y #add new character code
    h&=mask #remove any codes over the max code length
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
    #print (b,k,mask)
    m=len(string_1)
    n=len(string_2)
    #calculate the hash for the first k characters
    h=0
    for i in range(0,k):
        h=r_hash(h,characters[string_1[i]],b,k,mask)
    if h not in table:
        table[h]=[]
    table[h].append(0)
    for i in range(k,m):
        #for every new character update the hash
        h=r_hash(h,characters[string_1[i]],b,k,mask)
        if h not in table:
            table[h]=[]
        table[h].append(i-k+1) #append the start position to the list of the substring hash

    #calculate the hash for the first k characters
    h=0
    for i in range(0,k):
        h=r_hash(h,characters[string_2[i]],b,k,mask)
    if h in table:
        pairs.extend([(i,0,True) for i in table[h]]) #for every i index create i,0 pair
    for j in range(k,n):
        #for every new character update the hash
        h=r_hash(h,characters[string_2[j]],b,k,mask)
        if h not in table:
            continue
        pairs.extend([(i,j-k+1,True) for i in table[h]]) #for every i index create i,j pair

    r=len(pairs)

    pairs_e=[(i+k,j+k,False) for i,j,_ in pairs]
    pairs.extend(pairs_e) #create events starts are True ends are False
    pairs.sort() #sort in row major style ordering

    return pairs,r
