import sys

fname=sys.argv[1]
f=open(fname)
string1=""
line=f.readline()
while (line!=""):
    if line[0]!=">":
        string1+=line[0:-1]
    line=f.readline()
f.close()
fname=sys.argv[2]
f=open(fname)
string2=""
line=f.readline()
while (line!=""):
    if line[0]!=">":
        string2+=line[0:-1]
    line=f.readline()
f.close()
k=1
for i in [2,2,3,3,4,4,5,5,6,6]:
    f=open("Echerihia/fs"+str(i)+str(k),"w+")
    f.write(string1[k:k+10**i]+"\n")
    f.write(string2[k:k+10**i]+"\n")
    k=k+10**i
    f.close()
