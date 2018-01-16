#ifndef _LCSKPP_FENWICK_H_
#define _LCSKPP_FENWICK_H_

typedef struct {
    int first;
    int second;
} pair;

pair pairMax(pair a, pair b);

typedef struct {
    pair* values;
    int size;
} FenwickMax;

void FenwickMax_new(FenwickMax* fen, int size);
pair FenwickMax_get(FenwickMax* fen, int i);
void FenwickMax_set(FenwickMax* fen, int i, pair value);


#endif // _LCSKPP_FENWICK_H_