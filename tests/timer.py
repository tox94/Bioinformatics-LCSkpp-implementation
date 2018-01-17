from subprocess import call,check_output
import os
import sys
FNULL = open(os.devnull, 'w')
files=check_output(["ls","test_sequences"])
files_list=files.decode().split("\n")[0:-1]
p=["python","c","java","c++"]
pro=p[int(sys.argv[1])]
flag1=1
flag2=1
start=0
if pro=="java":
    flag1=0
    flag2=0
for k in [15,20,25]:
    if k==20:
        flag1=1
    for f in files_list:
        if flag1==1 and f=="fs6-1.txt":
            start=1
        if start==1:
            print (pro,k,f)
        if pro=="python":
            call_l=["/usr/bin/time","-v","-o","tested/"+pro+"_tested_k_"+str(k)+f, "python3", "../python/main.py", str(k), "test_sequences/"+f]
            call(call_l)
        elif pro=="java":
            if start==1:
                call_l=["/usr/bin/time","-v","-o","tested/"+pro+"_tested_k_"+str(k)+f, "java", "-cp", "../java/", "Main", "main", str(k), "test_sequences/"+f]
                call(call_l)
        elif pro=="c":
            call_l=["/usr/bin/time","-v","-o","tested/"+pro+"_tested_k_"+str(k)+f, "../c/main", "test_sequences/"+f,str(k)]
            call(call_l)
        elif pro=="c++":
            call_l=["/usr/bin/time","-v","-o","tested/"+pro+"_tested_k_"+str(k)+f,"../cpp/main","test_sequences/"+f,str(k)]
            call(call_l)
