void rech_ind_dicho(int tab[],int val_r){
    int ind = -1;
    int i_deb = 0;
    int i_fin = sizeof(tab)-1;
    while ((i_deb<=i_fin)&&(ind == -1)){
        i_mill(i_deb+i_fin)/2;
        if (val[i_mill]==val_r){
            int ind = i_mill;
        }
        else {
            if (tab[i_mill]>val_r){
                i_fin = i_mill-1;
            }
            else {
                i_deb=i_mill+1;
            }
        }
    }
    return ind;
}
