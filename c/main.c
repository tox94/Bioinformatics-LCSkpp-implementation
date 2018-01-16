#include <stdio.h>

#include "lcskpp.h"

int main(int argc, char const *argv[]) {
    FILE *file;
    file = fopen(argv[1],"r");
    char *a = NULL;
    char *b = NULL;
    size_t len = 0;
    getline(&a,&len,file);
    getline(&b,&len,file);

    int k = atoi(argv[2]);

    int rez;
    char ** recon = (char**) malloc(sizeof(char*));
    a[strlen(a)-1] = '\0';
    b[strlen(b)-1] = '\0';
    rez = lcskpp(a,b, k, recon);

    printf("%d\n", rez);
    printf("%s\n",a);
    printf("%s\n",b);
    printf("%s\n",*recon);
    //printf("%d\n",strlen(*recon));

    fclose(file);
    return 0;
}