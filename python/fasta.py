import sys

fname=sys.argv[1]
f=open(fname)
string1=""
line=f.readline()
while (line!=""):
    if m[0]!=">":
        string1+=m[0:-1]
    line=f.readline()
f.close()
fname=sys.argv[2]
f=open(fname)
string2=""
line=f.readline()
while (line!=""):
    if m[0]!=">":
        string2+=m[0:-1]
    line=f.readline()
f.close()
fname=sys.argv[3]
f=open(fname,"w+")
f.write(string_1+"\n")
f.write(string_2+"\n")
f.close()
