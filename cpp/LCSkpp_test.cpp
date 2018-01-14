#include <iostream>

#include "LCSkpp.h"

using namespace std;

int main(int argc, char const *argv[]) {
    
    string a="ABCDABC";
    string b="ABCEABC";
    int k=3;
    int lcskpp_value = LCSkpp(a,b,k); 
    
    cout<<lcskpp_value<<endl;

    return 0;
}
