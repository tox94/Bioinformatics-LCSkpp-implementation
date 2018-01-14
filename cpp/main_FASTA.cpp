#include <iostream>
#include <fstream>
#include <vector>

#include "LCSkpp.h"

using namespace std;


int main(int argc, char const *argv[]) {

    if(argc != 4) {
        cerr<< "Required 2 FASTA format files and k value"<<endl;
        return -1;
    }

    ifstream input1 (argv[1]);
    ifstream input2 (argv[2]);

    string line, id1, id2, a,b;

    while (getline(input1, line)) {

        if(line.empty())
            continue;

        if (line[0] == '>') {
            id1 = line.substr(1);
        }
        else {
            a += line;
        }
    }

        while (getline(input2, line)) {

        if(line.empty())
            continue;

        if (line[0] == '>') {

            id2 = line.substr(1);
        }
        else {
            b += line;
        }
    }

    int k=atoi(argv[3]);
    int lcskpp_value = LCSkpp(a,b,k); 
    
    cout<<lcskpp_value<<endl;

    return 0;
}
