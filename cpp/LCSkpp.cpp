/**
 
  @author: Mihovil Kucijan
 
 */
#include <vector>
#include <string>
#include <unordered_map>
#include <tuple>
#include <algorithm>

#include "LCSkpp.h"
#include "FenwickMaxTree.h"

#include <iostream>

//construct dictionary for every type of character in given strings
//and give it byte label starting from 0.
std::unordered_map<char,uint8_t> alphabet(std::string& a, std::string& b) {
    size_t size = 0;
    std::unordered_map<char, uint8_t> ret ;

    for(size_t i = 0; i<a.size(); i++) {
        if (ret.find(a[i])==ret.end())
            ret[a[i]]=size++;
    }
    for(size_t i = 0; i<b.size(); i++) {
        if (ret.find(b[i])==ret.end())
            ret[b[i]]=size++;
    }
    
    return ret;
}

std::vector<std::tuple<int,int,bool>>* get_events(
                                        std::string& a, std::string& b, int k, 
                                        Map2D& matchPairs) {
    
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
    for(int i=k-1; i<b.size(); i++) {
        hash = hash*alphabet_size + code[b[i]];
        hash %= mod;

        auto a_indexes = a_index.equal_range(hash);
        int j = i -(k-1);
        for(auto it=a_indexes.first; it!=a_indexes.second; it++) {
            events->push_back(std::make_tuple(it->second+k, j+k, false)); //end of substring
            events->push_back(std::make_tuple(it->second,j,true));       //start of substring
            matchPairs[std::make_pair(it->second,j)]=count++;
        }
    }
    
    std::sort(events->begin(), events->end());

    return events;
}

int LCSkpp(std::string& a, std::string& b, const int k) {
    Map2D matchPairs;
    auto events = get_events(a, b, k, matchPairs);
    
    int n = b.size() + 1;
    FenwickMaxTree dpColMax(n);

    std::vector<int> dp(matchPairs.size());

    int maxDp = 0;

    for(auto event=events->begin(); event!=events->end(); event++) {
        int i = std::get<0>(*event);
        int j = std::get<1>(*event);
        bool start = std::get<2>(*event);

        if (start) {
            std::pair<int,int> i_j = std::make_pair(i,j);
            dp[matchPairs[i_j]] = dpColMax.getMax(j) + k;
        
        } else {
            std::pair<int,int> i_j = std::make_pair(i-k,j-k);
            auto iprev_jprev = std::make_pair(i-1-k,j-1-k); // i,j is end of substring, 
                                                            // we need to lookup does start of prev exists
            if (matchPairs.find(iprev_jprev) != matchPairs.end()) {
                dp[matchPairs[i_j]] = std::max( dp[matchPairs[iprev_jprev]]+1, dp[matchPairs[i_j]] );

            }    

            dpColMax.setValue(j,dp[matchPairs[i_j]]);


            maxDp = std::max(dp[matchPairs[i_j]], maxDp);
        }
    }

    return maxDp; 
}


