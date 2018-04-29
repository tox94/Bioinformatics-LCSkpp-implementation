#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

#include "lcskpp.h"

uint8_t* getAlphabet(char* a, char* b, uint8_t* size) {
    uint8_t* ret;
    ret = (uint8_t*) malloc(256*sizeof(uint8_t));
    int i, pomSize=0;
    for(i=0; i<256; i++) ret[i]=255;

    int m=strlen(a);
    for(i=0; i<m; i++) {
        if(ret[a[i]]==255) {
            ret[a[i]]=(pomSize);
            (pomSize) += 1;
        }

    }

    int n=strlen(b);
    for(i=0; i<n; i++) {
        if(ret[b[i]]==255) {
            ret[b[i]]=(pomSize);
            pomSize += 1;
        }
    }
    *size = pomSize;
    return ret;
}

//event sort
int compare(const void *e1, const void *e2) {
    event_t *s1 = (event_t *)e1;
    event_t *s2 = (event_t *)e2;
    if((s2->i) < (s1->i)) {
        return 1;
    } else if ((s2->i) == (s1->i)) {
        if ((s2->j) < (s1->j)) {
            return 1;
        } else if ((s2->j) == (s1->j)) {
            if ((s2->start) < (s1->start)) {
                return 1;
            } else if ((s2->start) == (s1->start)) {
                return 0;
            } else {
                return -1;
            }
        } else {
            return -1;
        }
    } else {
        return -1;
    }

}

void getMatches(char *a, char *b, int k, event_t **events_p, MapHash_t** matches_p, int* numMatches) {
    uint8_t AlphabetSize;
    event_t * events = NULL;
    uint8_t* alphabet = getAlphabet(a,b, &AlphabetSize);
    uint64_t mod = 1;
    uint64_t hash = 0;

    Bucket_t *aMap = NULL;
    int i;
    uint64_t size = AlphabetSize;

    //mod for rolling hash
    //AlphabetSize ^ k number of substrings
    // should be lower then 2^64 
    if(AlphabetSize == 4) {
        mod = mod<<(2*k);
    } else {
        for(i=0; i<k; i++){
            mod = mod * size;
        }
    }

    for(i=0; i<k-1; i++) {
        hash = hash*AlphabetSize + alphabet[a[i]];
        hash %= mod;                            //calculating prefix of the first substring
    }
    Bucket_t *s;
    int* index;
    int m=strlen(a);
    for(i=k-1; i<m; i++) {
        hash = hash*AlphabetSize + alphabet[a[i]];
        hash %= mod;
        //HASH_FIND_INT(aMap, &hash, s);
        HASH_FIND(hh, aMap, &hash, sizeof(uint64_t), s);
        if (s==NULL) { //adding bucket 
            s = (Bucket_t*)malloc(sizeof(Bucket_t));
            vector_init(&(s->v));
            s->key = hash;
            //HASH_ADD_INT(aMap, key, s);
            HASH_ADD(hh, aMap, key, sizeof(uint64_t), s);
        }
        index = (int *) malloc(sizeof(int));
        *index = i-k+1; //start of substring should be added
        vector_add(&(s->v),index);
    }

    hash = 0;
    for(i=0; i<k-1; i++) {
        hash = hash*AlphabetSize + alphabet[b[i]];
        hash %= mod;                            //calculating prefix of the first substring
    }

    *numMatches = 0;
    MapHash_t *matches = NULL;
    int n=strlen(b);
    for(i=k-1; i<n; i++) {
        hash = hash*AlphabetSize + alphabet[b[i]];
        hash %= mod;
        //HASH_FIND_INT(aMap, &hash, s);
        HASH_FIND(hh, aMap, &hash, sizeof(uint64_t), s);
        if (s==NULL) { //substring doesnt exist in first string
            continue;
        } else {
            int j;
            int vec_size = vector_count(&(s->v));
            for (j = 0; j < vec_size; j++) {
                *numMatches += 1;
                int a_i = *((int*) vector_get(&(s->v),j));
                events = (event_t *) realloc(events, 2*(*numMatches)*sizeof(event_t));
                if(events != NULL) { //adding start and end indices in the event list
                    events[(*numMatches)*2-2].i=a_i;
                    events[(*numMatches)*2-2].j=i-k+1;
                    events[(*numMatches)*2-2].start=true;
                    events[(*numMatches)*2-1].i=a_i+k;
                    events[(*numMatches)*2-1].j=i+1;
                    events[(*numMatches)*2-1].start=false;
                } else {
                    printf("Problem.\n");
                }
                MapHash_t* newMatch = (MapHash_t *)malloc(sizeof(MapHash_t));
                //memset(newMatch, 0, sizeof(MapHash_t));
                (newMatch->key).first=a_i;
                (newMatch->key).second=i-k+1;
                (newMatch->index)=(*numMatches)-1; //matchPair index for searching through arrays
                HASH_ADD(hh, matches, key, sizeof(pair), newMatch);
            }
        }
    }
    qsort(events, (*numMatches)*2, sizeof(event_t), compare);
    *events_p = events;
    *matches_p = matches;

    return;
}

//concatenate strings
char* stradd(const char* a, const char* b){
    size_t len = strlen(a) + strlen(b);
    char *ret = (char*)malloc(len * sizeof(char) + 1);
    *ret = '\0';
    return strcat(strcat(ret, a) ,b);
}

void reconstruct(char* a, char* b, int const k, int *prev_index, pair* indices,
                pair maxDp, char** reconstructed) {

    int index = maxDp.second;
    int i_prev = indices[index].first;
    int i=i_prev +k;
    char * ret = (char*)malloc(sizeof(char));
    *ret = '\0';
    while(i_prev != -1) {
        if(i-i_prev<=k) {
            char *buff;
            buff = (char *) malloc(sizeof(char)*(k+1));
            memset(buff, 0, sizeof(char)*(k+1));
            memcpy( buff, &a[i_prev], i-i_prev );
            ret = stradd(buff,ret);
        } else {
            char *buff;
            buff = (char *) malloc(sizeof(char)*(k+2));
            memset(buff, 0, sizeof(char)*(k+2));
            buff[k]='-';
            memcpy( buff, &a[i_prev], k );
            ret = stradd(buff,ret);
        }
        i = i_prev;
        index = prev_index[index];
        if (index == -1) {
            break;
        }
        i_prev = indices[index].first; //traceback list of origin of the value
    }

    *reconstructed = ret;
    return;
}

int lcskpp(char* a, char* b, const int k, char** reconstructed) {
    event_t** events_p = (event_t **) malloc(sizeof(event_t *));
    MapHash_t** matches_p = (MapHash_t **) malloc(sizeof(MapHash_t *));
    int numMatches;

    getMatches(a,b,k,events_p,matches_p,&numMatches);

    //no matches or k too big
    if ((numMatches)==0) {
        char* recon = (char *) malloc(sizeof(char));
        *recon = '\0';
        *reconstructed = recon;
        return 0;
    }
    event_t* events = *events_p;
    MapHash_t* matches = *matches_p;

    int *dp;
    dp = (int *) malloc(sizeof(int)*numMatches);
    memset(dp , 0, sizeof(int)*numMatches);
    int *prev_index;
    prev_index = (int *) malloc(sizeof(int)*numMatches);
    memset(prev_index, -1, sizeof(int)*numMatches);
    pair *indices;
    indices = (pair *) malloc(sizeof(pair)*numMatches);

    pair maxDp;
    maxDp.first = 0;
    maxDp.second = -1;

    int n = strlen(b);

    FenwickMax dpColMax;
    FenwickMax_new(&dpColMax, n);
    int i;
    int eventSize = numMatches*2;
    for(i=0; i<eventSize; i++) {
        event_t event = events[i];
        int i = event.i;
        int j = event.j;
        bool start = event.start;

        if (start) {
            pair matchIndex;
            matchIndex.first = i;
            matchIndex.second = j;
            pair maxCol = FenwickMax_get(&dpColMax, j); // searching max of left top corner of the map
            MapHash_t *p;
            HASH_FIND(hh, matches, &matchIndex, sizeof(pair), p);
            dp[p->index] = maxCol.first + k; // current maximum sequence is with this substring longer for k

            prev_index[p->index] = maxCol.second;
            indices[p->index].first = i;
            indices[p->index].second = j;
        } else {
            pair matchIndex, matchIndexPrev;
            matchIndex.first = i-k; //start of substring
            matchIndex.second = j-k;
            matchIndexPrev.first = i-k-1;  //if substring continues it is one before on the same diagonal
            matchIndexPrev.second = j-k-1;
            MapHash_t *p,*pPrev;
            HASH_FIND(hh, matches, &matchIndex, sizeof(pair), p);
            HASH_FIND(hh, matches, &matchIndexPrev, sizeof(pair), pPrev);
            if (pPrev != NULL) { 
                if((dp[pPrev->index]+1)> dp[p->index]) { //current value can still be bigger
                    dp[p->index] = dp[pPrev->index]+1;   // (if adding to preceding substring)
                    prev_index[p->index] = pPrev->index;
                }
            }

            pair cur;
            cur.first = dp[p->index];
            cur.second = p->index;
            FenwickMax_set(&dpColMax,j, cur); // updating left top area

            maxDp = pairMax(maxDp, cur);
        }
    }
    if (numMatches==0) return 0;
    reconstruct(a, b, k, prev_index, indices, maxDp, reconstructed);

    return maxDp.first;
}
