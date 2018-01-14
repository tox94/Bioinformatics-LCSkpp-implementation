#include <iostream>
#include <fstream>
#include <vector>

#include "LCSkpp.h"

using namespace std;


int main(int argc, char const *argv[]) {
    if(argc != 4) {
        cerr<< "Required 2 FASTQ format files and k value"<<endl;
        return -1;
    }

    ifstream input1 (argv[1]);
    ifstream input2 (argv[2]);

    string line, id , a, b;
    
    int i=0;
    while (std::getline(input1, line)) {
        if(i%4==1) {
            a += line;
        } 
        else {
            continue;
        }
    }

    while (std::getline(input2, line)) {
        if(i%4==1) {
            a += line;
        } 
        else {
            continue;
        }
    }

    int k=atoi(argv[3]);
    int lcskpp_value = LCSkpp(a,b,k); 
    
    cout<<lcskpp_value<<endl;

    return 0;
}
