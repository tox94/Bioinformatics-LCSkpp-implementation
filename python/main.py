from lcskpp import LCSkpp
import sys

def main():
    if len(sys.argv)<3:
        print ("Please define k and input file")
        return
    k=int(sys.argv[2])
    file=open(sys.argv[1])
    string_1=file.readline().strip().lower()
    string_2=file.readline().strip().lower()
    file.close()
    LCSkpp(k,string_1,string_2)

if __name__ == '__main__':
    main()
