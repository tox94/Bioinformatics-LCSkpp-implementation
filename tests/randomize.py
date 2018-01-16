import random
import sys

num_s=int(sys.argv[1])

alfa=["A","C","G","T"]


for l in [2,3,4,5,6]:
    strings=[["",""] for i in range(num_s)]
    print (l)
    for i in range(10**l):
        for s in range(len(strings)):
            strings[s][0]+=alfa[random.randrange(4)]
            strings[s][1]+=alfa[random.randrange(4)]

    for s in range(len(strings)):
        file=open("test_sequences/fs"+str(l)+"-"+str(s)+".txt","w")
        file.write(strings[s][0]+"\n")
        file.write(strings[s][1]+"\n")
        file.close()
