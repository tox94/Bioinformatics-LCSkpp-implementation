import random
import sys

alfa=["A","C","G","T"]
s1=s2=""

for i in range(int(sys.argv[1])):
    s1+=alfa[random.randrange(3)]
    s2+=alfa[random.randrange(3)]

file=open("fs.txt","w")
file.write(s1+"\n")
file.write(s2+"\n")
file.close()
