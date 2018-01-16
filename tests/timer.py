from subprocess import call,check_output
import os
FNULL = open(os.devnull, 'w')
files=check_output(["ls","test_sequences"])
files_list=files.decode().split("\n")[0:-1]
for k in [15,20,25]:
    for f in files_list:
        print (k,f)
        call_l=["/usr/bin/time","-v","-o","tested/python_tested_k_"+str(k)+f,"python3", "../python/main.py",str(k),"test_sequences/"+f]
        call(call_l)
