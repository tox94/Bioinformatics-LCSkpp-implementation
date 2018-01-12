from Math import log
def setup_characters(x,y):
    characters={}
    i=1
    for x_c in x:
        if x_c not in characters:
            characters[x_c]=i
            i+=1
    for y_c in y:
        if y_c not in characters:
            characters[y_c]=i
            i+=1
    b=log(i,2)
    return  b,characters

def r_hash(x,y,k):
    pass

def MatchPairs(string_1,string_2):
    for i in range(len(string)-k)
        table[hash(string[i:i+k])].append(i)
    for i in range(len(string2)-k)
        lista_parova.append([(i,j) for j in table[hash(string2[i:i+k]]))
