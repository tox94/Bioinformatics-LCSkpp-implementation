#ifndef _LCSKPP_FENWICKMAXTREE_H_
#define _LCSKPP_FENWICKMAXTREE_H_

#include <vector>

class FenwickMaxTree {

public:
    FenwickMaxTree(size_t size) {
        values = std::vector<int>(size+1, 0);
    }

    int getMax(size_t i) {
        i++;

        int max_value = 0;

        while(i>0) {
            max_value = std::max(values[i],max_value);
            i = getPrevious(i);
        }

    }

    void setValue(size_t i, int new_value) {
        i++;
        while(i<values.size()) {
            values[i] = std::max(values[i], new_value);
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
    std::vector<int> values;


};

#endif // _FENWICKMAXTREE_H_
