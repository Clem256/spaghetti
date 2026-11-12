#include <stdio.h>    // printf
#include <stdlib.h>   // malloc, free

void procedure();

int var_globale, var_globale_init = 42;

int main(int argc, char **argv)
{
    static char var_statique, var_statique_init = 'A';
    char *pt_tab, *pt_c;

    printf("\npile (stack)\n");
    printf("     fonction main\n");
    printf("\t\tpremier parametre formel             adresse : %p\n", &argc);
    printf("\t\tsecond parametre formel            adresse : %p\n", &argv);
    printf("\t\tpremiere variable locale             adresse : %p\n", &pt_tab);
    printf("\t\tseconde variable locale             adresse : %p\n\n", &pt_c);

    procedure();

    printf("\ntas (heap)\n");
    pt_tab = (char*)malloc(1024 * sizeof(char));
    pt_c = (char*)malloc(sizeof(char));

    if (pt_c == NULL)
        printf("Erreur d'allocation, le caractere n'a pas ete cree.\n");
    else
        printf("\tallocation dynamique d'un caractere                    adresse : %p\n", pt_c);

    if (pt_tab == NULL)
        printf("Erreur d'allocation, le tableau de caracteres n'a pas ete cree.\n");
    else
        printf("\tallocation dynamique d'un tableau                      adresse : %p\n", pt_tab);

    printf("\nvariables globales et statiques non initialisees (bss)\n");
    printf("\tvariable globale non initialisee                       adresse : %p\n", &var_globale);
    printf("\tvariable statique non initialisee                      adresse : %p\n", &var_statique);

    printf("\nvariables globales et statiques initialisees (data)\n");
    printf("\tvariable statique initialisee                          adresse : %p\n", &var_statique_init);
    printf("\tvariable globale initialisee                           adresse : %p\n", &var_globale_init);

    printf("\ncode (text)\n");
    printf("\tinstructions de la fonction procedure                  adresse : %p\n", procedure);
    printf("\tinstructions de la fonction main                       adresse : %p\n", main);

    if (pt_tab != NULL)
        free(pt_tab);
    if (pt_c != NULL)
        free(pt_c);

    return(0);
}


void procedure()
{
    static int var_statique = 0;
    int var_1, var_2;

    if (++var_statique == 4)     // On limite l'appel récursif à 3.
        return;

    printf("     fonction procedure recursive, appel numero %d\n", var_statique);
    printf("\t\tpremiere variable locale             adresse : %p\n", &var_1);
    printf("\t\tseconde variable locale             adresse : %p\n", &var_2);
    printf("\tvariable statique initialisee                          adresse : %p\n", &var_statique);

    procedure();                       // appel récursif
}
