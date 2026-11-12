#include <stdio.h>
#include <stdlib.h>

void procedure();
int var_globale,var_globale_init = 42;
int main(int argc,char**argv){
    static char var_statique , var_statique_init = 'A';
    char *pt_tab,*pt_c;
    printf("\n pile (stack) \n");
    printf("  fonction main \n");
    printf("\t\t premier parametre formel   adresse : %p\n",&argc);
    printf("\t\t second parametre formel   adresse : %p\n",&argv);
    printf("\t\t première variable locale   adresse : %p\n",&pt_tab);
    printf("\t\t seconde variable locale   adresse : %p\n",&pt_c);
    procedure();
    printf("\n tas (heap) \n");
}
