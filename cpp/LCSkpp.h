#ifndef _LCSKPP_H_
#define _LCSKPP_H_

#include <vector>
#include <string>
#include <unordered_map>

#include "FenwickMaxTree.h"

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



#endif // _LCSKPP_H_
