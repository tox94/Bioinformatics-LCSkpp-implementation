from lcskpp import LCSkpp
import sys

def main():
    if len(sys.argv)<2:
        print ("Please define k")
        return
    k=int(sys.argv[1])
    file=open("strings.txt")
    string_1=file.readline().strip()
    string_2=file.readline().strip()
    maximum_length=LCSkpp(k,string_1,string_2)
    print (maximum_length)
if __name__ == '__main__':
    main()
