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

typedef std::pair<int,std::pair<int,int>> dpType;

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

void reconstruct(std::string& a, std::string& b, int k,
                std::vector<int>& dp, std::vector<std::pair<int,int>>& prev,
                Map2D& matchPairs,dpType& dpMax, std::string& reconstructed);

int LCSkpp(std::string& a, std::string& b, const int k, std::string& reconstructed);

#endif // _LCSKPP_H_

