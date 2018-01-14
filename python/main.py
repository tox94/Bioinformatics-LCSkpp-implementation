from lcskpp import LCSkpp
import sys

def main():
    if len(sys.argv)<3:
        print ("Please define k and input file")
        return
    k=int(sys.argv[1])
    file=open(sys.argv[2])
    string_1=file.readline().strip().lower()
    string_2=file.readline().strip().lower()
    file.close()
    maximum_length=LCSkpp(k,string_1,string_2)
    print (maximum_length)
if __name__ == '__main__':
    main()
