void fusionner(double tab[],int i_deb,int i_mill,int i_fin){
  //ligne à trouver à partir de l'algo  temp=zeros(i_fin-i_fin+1,float)
    int i=i_deb;
    int j=i_mill+1;
    int k=0;
    while ((i<i_mill)&&(j<=i_fin)){
        if (tab[i]<tab[j]){
            temp[k]=tab[i];
            i=i+1;
        }
        else {
            temp[k]=tab[j];
            j=j+1;
        }
        k=k+1;
    }
    while(i<=i_mill){
        temp[k]=tab[j];
        i=i+1;
        k=k+1;
    }
    while (j<=i_fin){
        temp[k]=tab[j];
        j=j+1;
        k=k+1;
    }
    k=0;
    while (k<len(temp)){
        tab[i_deb+k]=temp[k];
        k=k+1;
    }
    return 0;
}
void tri_fusion(double tab[],int i_deb , int i_fin){
    int i_mill=(i_deb+i_fin)/2;
    if(i_deb<i_fin){
        tri_fusion(tab,i_deb,i_mill);
        tri_fusion(tab,i_mill+1,i_fin);
        fusionner(tab,i_deb,i_mill,i_fin);
    }
}
