package com.mycompany.qualitedev.model;

import java.util.List;

/** Un Pokémon : identité, types (le 2e est facultatif), PV et attaques. */
public class Pokemon {

    public static final int PV_PAR_DEFAUT = 100;

    private final String nom;
    private final TypePokemon type1;
    private final TypePokemon type2; // peut être null
    private final String cheminImage;
    private final List<Attaque> attaques;
    private final int pvMax;
    private int pv;

    public Pokemon(String nom, TypePokemon type1, TypePokemon type2, String cheminImage, List<Attaque> attaques) {
        this.nom = nom;
        this.type1 = type1;
        this.type2 = type2;
        this.cheminImage = cheminImage;
        this.attaques = List.copyOf(attaques);
        this.pvMax = PV_PAR_DEFAUT;
        this.pv = pvMax;
    }

    /** Multiplicateur total d'une attaque de ce type contre ce Pokémon (les deux types se cumulent). */
    public double multiplicateurContre(TypePokemon typeAttaque) {
        double m = typeAttaque.multiplicateurContre(type1);
        if (type2 != null) m *= typeAttaque.multiplicateurContre(type2);
        return m;
    }

    /** Applique une attaque à ce Pokémon et retourne les dégâts réellement infligés. */
    public int recevoir(Attaque attaque) {
        int degats = (int) (attaque.degats() * multiplicateurContre(attaque.type()));
        pv = Math.max(0, pv - degats);
        return degats;
    }

    public boolean estKO() {
        return pv == 0;
    }

    public String getNom() { return nom; }
    public TypePokemon getType1() { return type1; }
    public TypePokemon getType2() { return type2; }
    public String getCheminImage() { return cheminImage; }
    public List<Attaque> getAttaques() { return attaques; }
    public int getPv() { return pv; }
    public int getPvMax() { return pvMax; }
}
