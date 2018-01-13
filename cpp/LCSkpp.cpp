#include <vector>
#include <string>
#include <unordered_map>
#include <tuple>
#include <algorithms>

#include "LCSkpp.h"
#include "FenwickMaxTree.h"

//construct dictionary for every type of character in given strings
//and give it byte label starting from 0.
std::unordered_map<char,uint8_t> alphabet(std::string& a, std::string& b) {
    size_t size = 0;
    std::unordered_map<char, uint8_t> ret ;

    for(size_t i = 0; i<a.size(); i++) {
        if (!ret[a[i]])
            ret[a[i]]=size++;
    }
    for(size_t i = 0; i<b.size(); i++) {
        if (!ret[b[i]])
            ret[b[i]]=size++;
    }

    return ret;
}

std::vector<std::tuple<int,int,int>>* get_events(std::string& a, std::string& b, int k) {
    
    std::unordered_map<char,uint8_t> code=alphabet(a,b);
    int alphabet_size = code.size();

    // using rabin karp for k length substring alphabet_size**k posible substrings
    uint64_t mod = 1;
    uint64_t hash = 0;
    std::unordered_multimap<uint64_t, int> a_index;

    for(int i=0; i<k; i++) mod *= alphabet_size;

    for(int i=0; i<k-1; i++) {
        hash = hash*alphabet_size + code[a[i]];
        hash %= mod;                            //calculating prefix of the first substring
    }

    for(int i=k-1; i<a.size(); i++) {
        hash = hash*alphabet_size + code[a[i]];
        hash %= mod;

        a_index.insert({hash, i-(k-1)}); // adding start indexes of substring for whole first substring
    }

    hash = 0;
    for(int i=0; i<k-1; i++) {
        hash = hash*alphabet_size + code[b[i]];
        hash %= mod;                            //calculating prefix of the first substring
    }

     auto events = new std::vector<std::tuple<int,int,int>>();

     for(int i=0; i<k-1; i++) {
        hash = hash*alphabet_size + code[b[i]];
        hash %= mod;

        auto a_indexes = a_index.equal_range(hash);
        int j = i -(k-1);
        for(auto it=a_indexes.first; it!=a_indexes.second; it++) {
            events->push_back(std::make_tuple(it->second+k, j+k, 0)); //end of substring
            events->push_back(std::make_tuple(it->second,j,1));       //start of substring
        }
    }
    
    std::sort(events->begin(), events->end());

    return events;
}


