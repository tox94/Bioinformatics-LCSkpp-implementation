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

std::vector<std::tuple<int,int,bool>>* get_events(
                                        std::string& a, std::string& b, int k, 
                                        std::map<pair<int,int>,int>& matchPairs) {
    
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

    auto events = new std::vector<std::tuple<int,int,bool>>();

    int count = 0;
    for(int i=0; i<k-1; i++) {
        hash = hash*alphabet_size + code[b[i]];
        hash %= mod;

        auto a_indexes = a_index.equal_range(hash);
        int j = i -(k-1);
        for(auto it=a_indexes.first; it!=a_indexes.second; it++) {
            events->push_back(std::make_tuple(it->second+k, j+k, false)); //end of substring
            events->push_back(std::make_tuple(it->second,j,true));       //start of substring
            matchPairs[{it->second,j}]=count++;
        }
    }
    
    std::sort(events->begin(), events->end());


    return events;
}

int LCSkpp(std::string& a, std::string& b, const int k) {
    std::map<pair<int,int>,int> matchPairs;
    auto events = get_events(a,b, k, matchPairs);
    
    int n = b.size();
    FenwickMaxTree dpColMax(n);

    vector<int> dp(matchPairs.size());

    int maxDp = 0;

    for(auto event=events.begin(); event!=events.end(); event++) {
        int i = event->get(0);
        int j = event->get(1);
        bool start = event->get(2);


        if (start) {
        
            dp[matchPairs[{i,j}]] = dpColMax.getMax(j) + k;
        
        } else {
            if (matchPairs.find({i-1,j-1}) != matchPairs.end()) {
                dp[matchPairs[{i,j}]] = std::max({ dp[matchPairs[{i-1,j-1}]]+1, dp[matchPairs[{i, j}]] })
            }    

            dpColMax.setValue(j,dp[matchPairs[{i,j}]]);

            maxDp = std::max({dp[matchPairs[{i,j}]], maxDp});
        }
    }

    return maxDp; 
}


