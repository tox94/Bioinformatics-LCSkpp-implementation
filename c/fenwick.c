#include <stdlib.h>

#include "fenwick.h"


pair pairMax(pair a, pair b) {
    if(a.first>b.first) {
        return a;
    } else {
        return b;
    }
}


void FenwickMax_new(FenwickMax* fen, int size) {
    size++;
    fen->size = size;
    fen->values = (pair*) malloc(size*sizeof(pair));
    int i;
    for(i=0; i<size; i++) {
        (fen->values[i]).first = 0;
        (fen->values[i]).second = -1;
    }
}

pair FenwickMax_get(FenwickMax* fen, int i) {
    i++;
    pair max;
    max.first = 0;
    max.second = -1;
    while(i>0) {
        max = pairMax(fen->values[i],max);
        
        i -= ((-i)&i);
    }
    
    return max;
}

void FenwickMax_set(FenwickMax* fen, int i, pair value) {
    i++;
    while(i<(fen->size)) {
        fen->values[i] = pairMax(fen->values[i], value);
        i += ((-i)&i);
    }
    
    return;
}

