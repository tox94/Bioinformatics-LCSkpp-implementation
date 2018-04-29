from subprocess import call,check_output
import os
import sys
FNULL = open(os.devnull, 'w')
files=check_output(["ls",sys.argv[1]])
files_list=files.decode().split("\n")[0:-9]
p=["python","c","java","c++","test"]
table={}

for pro in p:
    for k in [15,20,25]:
        for f in files_list:
            if "fs"!=f[0:2]:
                continue
            print (pro,k,f)
            if pro=="python":
                call_l=["/usr/bin/time","-v","-o",sys.argv[1]+"tested/"+pro+"_tested_k_"+str(k)+f, "python3", "../python/main.py", sys.argv[1]+f, str(k)]
                call(call_l)
                fi=open("py_output.txt")
                fi.readline()
                fi.readline()
                maxVal=fi.readline()
                fi.close()
                table[(k,f)]=[maxVal]
            elif pro=="java":
                call_l=["/usr/bin/time","-v","-o",sys.argv[1]+"tested/"+pro+"_tested_k_"+str(k)+f, "java", "-cp", "../java/", "Main", "main", sys.argv[1]+f, str(k)]
                call(call_l)
                fi=open("java_output.txt")
                fi.readline()
                fi.readline()
                maxVal=fi.readline()
                fi.close()
                table[(k,f)].append(maxVal)
            elif pro=="c":
                call_l=["/usr/bin/time","-v","-o",sys.argv[1]+"tested/"+pro+"_tested_k_"+str(k)+f, "../c/main", sys.argv[1]+f, str(k)]
                call(call_l)
                fi=open("c_output.txt")
                maxVal=fi.readline()
                fi.close()
                table[(k,f)].append(maxVal)
            elif pro=="c++":
                call_l=["/usr/bin/time","-v","-o",sys.argv[1]+"tested/"+pro+"_tested_k_"+str(k)+f,"../cpp/main",sys.argv[1]+f, str(k)]
                call(call_l)
                fi=open("cpp_output.txt")
                maxVal=fi.readline()
                fi.close()
                table[(k,f)].append(maxVal)
            elif pro=="test":
                pom=("/usr/bin/time","-v","-o",sys.argv[1]+"tested/"+pro+"_tested_k_"+str(k)+f)
                call_l=["../../lcskpp/main",sys.argv[1]+f, str(k),">> out.txt"]
                call(call_l)
keys=keys=[key for key in table.keys()]
keys.sort()
f=open("opt.txt","w")
for key in keys:
    print (key,table[key])
    f.write(str(key)+str(table[key]))
f.close()
