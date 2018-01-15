/**
  Fenwick data structure for calculating 
  maximum value of first i elements in an
  array.
 
  @author: Mihovil Kucijan
 
 */
#ifndef _LCSKPP_FENWICKMAXTREE_H_
#define _LCSKPP_FENWICKMAXTREE_H_

#include <vector>

typedef std::pair<int,std::pair<int,int>> dpType;

dpType dpMax(dpType First, dpType Second) {
    if (First.first>Second.first) {
        return First;
    } else {
        return Second;
    }
}


class FenwickMaxTree {

public:
    FenwickMaxTree(size_t size) {
        values = std::vector<dpType>(size+1,std::make_pair(0,std::make_pair(-1,-1)));
    }

    dpType getMax(size_t i) {
        i++;

        dpType max_value = std::make_pair(0,std::make_pair(-1,-1));
        while(i>0) {
            max_value = dpMax(values[i],max_value);
            i = getPrevious(i);
        }

        return max_value;
    }

    void setValue(size_t i, dpType new_value) {
        i++;
        while(i<values.size()) {
            values[i] = dpMax(values[i], new_value);
            i = getNext(i);

        }
    }


private:

    size_t lastBit(const size_t i) {
        size_t complement = (-i); //~i+1, second complement
        size_t lastBit = complement&i;
        
        return lastBit;
    }

    size_t getPrevious(const size_t i) {
        
        return i - lastBit(i);
    }

    size_t getNext(const size_t i) {
        
        return i+lastBit(i);
    }


private:
    std::vector<dpType> values;


};

#endif // _FENWICKMAXTREE_H_
