#ifndef _LCSKPP_H_
#define _LCSKPP_H_

#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>

#include "fenwick.h"
#include "uthash.h"
#include "vector.h"

typedef struct {
    int i;
    int j;
    bool start;
} event_t;


typedef struct {
    pair key;
    int index;
    UT_hash_handle hh;
} MapHash_t;

typedef struct {
    uint64_t key;
    vector v;
    UT_hash_handle hh;
} Bucket_t;

uint8_t* getAlphabet(char* a, char* b, uint8_t * size);

void getMatches(char *a, char *b, int k, event_t **events_p, MapHash_t** matches_p, int* numMatches);

int lcskpp(char* a, char* b, const int k, char** reconstructed);



#endif // _LCSKPP_H_
