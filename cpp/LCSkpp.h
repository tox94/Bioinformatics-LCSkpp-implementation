/**
  Implementation of LCSk++ similarity metric.

  LCSk++: A practical similarity metric for long strings
  (http://arxiv.org/pdf/1407.2407v1.pdf) 
  
  @author: Mihovil Kucijan
 
 */
#ifndef _LCSKPP_H_
#define _LCSKPP_H_

#include <vector>
#include <string>
#include <unordered_map>
#include <tuple>

#include "FenwickMaxTree.h"

struct pair_hash {
    inline std::size_t operator()(const std::pair<int,int> & v) const {
        return v.first*31+v.second;
    }
};

typedef std::unordered_map<std::pair<int,int>,int, pair_hash> Map2D;

std::unordered_map<char,uint8_t> alphabet(std::string& a, std::string& b);

std::vector<std::tuple<int,int,bool>>* get_events(
            std::string& a, std::string& b, int k,
            Map2D& matchPairs);

int LCSkpp(std::string& a, std::string& b, const int k);

#endif // _LCSKPP_H_

