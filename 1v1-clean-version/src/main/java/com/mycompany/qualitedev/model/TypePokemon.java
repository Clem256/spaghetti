package com.mycompany.qualitedev.model;

import java.text.Normalizer;
import java.util.EnumMap;
import java.util.Map;

/**
 * Les 18 types, avec le tableau d'efficacité (attaquant -> défenseur).
 * Multiplicateurs : 2.0 super efficace, 0.5 peu efficace, 0.0 aucun effet, 1.0 sinon.
 */
public enum TypePokemon {
    NORMAL("Normal"), FEU("Feu"), EAU("Eau"), ELECTRIQUE("Électrique"), PLANTE("Plante"),
    GLACE("Glace"), COMBAT("Combat"), POISON("Poison"), SOL("Sol"), VOL("Vol"),
    PSY("Psy"), INSECTE("Insecte"), ROCHE("Roche"), SPECTRE("Spectre"), DRAGON("Dragon"),
    TENEBRES("Ténèbres"), ACIER("Acier"), FEE("Fée");

    private static final Map<TypePokemon, Map<TypePokemon, Double>> TABLEAU = new EnumMap<>(TypePokemon.class);

    static {
        definir(NORMAL,     new TypePokemon[]{},                                  new TypePokemon[]{ROCHE, ACIER},                                     new TypePokemon[]{SPECTRE});
        definir(FEU,        new TypePokemon[]{PLANTE, GLACE, INSECTE, ACIER},     new TypePokemon[]{FEU, EAU, ROCHE, DRAGON},                          new TypePokemon[]{});
        definir(EAU,        new TypePokemon[]{FEU, SOL, ROCHE},                   new TypePokemon[]{EAU, PLANTE, DRAGON},                              new TypePokemon[]{});
        definir(ELECTRIQUE, new TypePokemon[]{EAU, VOL},                          new TypePokemon[]{ELECTRIQUE, PLANTE, DRAGON},                       new TypePokemon[]{SOL});
        definir(PLANTE,     new TypePokemon[]{EAU, SOL, ROCHE},                   new TypePokemon[]{FEU, PLANTE, POISON, VOL, INSECTE, DRAGON, ACIER}, new TypePokemon[]{});
        definir(GLACE,      new TypePokemon[]{PLANTE, SOL, VOL, DRAGON},          new TypePokemon[]{FEU, EAU, GLACE, ACIER},                           new TypePokemon[]{});
        definir(COMBAT,     new TypePokemon[]{NORMAL, GLACE, ROCHE, TENEBRES, ACIER}, new TypePokemon[]{POISON, VOL, PSY, INSECTE, FEE},               new TypePokemon[]{SPECTRE});
        definir(POISON,     new TypePokemon[]{PLANTE, FEE},                       new TypePokemon[]{POISON, SOL, ROCHE, SPECTRE},                      new TypePokemon[]{ACIER});
        definir(SOL,        new TypePokemon[]{FEU, ELECTRIQUE, POISON, ROCHE, ACIER}, new TypePokemon[]{PLANTE, INSECTE},                              new TypePokemon[]{VOL});
        definir(VOL,        new TypePokemon[]{PLANTE, COMBAT, INSECTE},           new TypePokemon[]{ELECTRIQUE, ROCHE, ACIER},                         new TypePokemon[]{});
        definir(PSY,        new TypePokemon[]{COMBAT, POISON},                    new TypePokemon[]{PSY, ACIER},                                       new TypePokemon[]{TENEBRES});
        definir(INSECTE,    new TypePokemon[]{PLANTE, PSY, TENEBRES},             new TypePokemon[]{FEU, COMBAT, POISON, VOL, SPECTRE, ACIER, FEE},    new TypePokemon[]{});
        definir(ROCHE,      new TypePokemon[]{FEU, GLACE, VOL, INSECTE},          new TypePokemon[]{COMBAT, SOL, ACIER},                               new TypePokemon[]{});
        definir(SPECTRE,    new TypePokemon[]{PSY, SPECTRE},                      new TypePokemon[]{TENEBRES},                                         new TypePokemon[]{NORMAL});
        definir(DRAGON,     new TypePokemon[]{DRAGON},                            new TypePokemon[]{ACIER},                                            new TypePokemon[]{FEE});
        definir(TENEBRES,   new TypePokemon[]{PSY, SPECTRE},                      new TypePokemon[]{COMBAT, TENEBRES, FEE},                            new TypePokemon[]{});
        definir(ACIER,      new TypePokemon[]{GLACE, ROCHE, FEE},                 new TypePokemon[]{FEU, EAU, ELECTRIQUE, ACIER},                      new TypePokemon[]{});
        definir(FEE,        new TypePokemon[]{COMBAT, DRAGON, TENEBRES},          new TypePokemon[]{FEU, POISON, ACIER},                               new TypePokemon[]{});
    }

    private final String libelle;

    TypePokemon(String libelle) {
        this.libelle = libelle;
    }

    private static void definir(TypePokemon attaquant, TypePokemon[] superEfficace,
                                TypePokemon[] peuEfficace, TypePokemon[] sansEffet) {
        Map<TypePokemon, Double> ligne = new EnumMap<>(TypePokemon.class);
        for (TypePokemon t : superEfficace) ligne.put(t, 2.0);
        for (TypePokemon t : peuEfficace) ligne.put(t, 0.5);
        for (TypePokemon t : sansEffet) ligne.put(t, 0.0);
        TABLEAU.put(attaquant, ligne);
    }

    /** Multiplicateur de dégâts d'une attaque de ce type contre un Pokémon de type {@code defenseur}. */
    public double multiplicateurContre(TypePokemon defenseur) {
        return TABLEAU.get(this).getOrDefault(defenseur, 1.0);
    }

    /** Retrouve un type depuis du texte, sans tenir compte de la casse ni des accents ("electrique" marche). */
    public static TypePokemon depuisTexte(String texte) {
        String cible = normaliser(texte);
        for (TypePokemon t : values()) {
            if (normaliser(t.libelle).equals(cible)) return t;
        }
        throw new IllegalArgumentException("Type inconnu : " + texte);
    }

    private static String normaliser(String s) {
        return Normalizer.normalize(s.trim(), Normalizer.Form.NFD)
                .replaceAll("\\p{M}", "")
                .toLowerCase();
    }

    @Override
    public String toString() {
        return libelle;
    }
}
