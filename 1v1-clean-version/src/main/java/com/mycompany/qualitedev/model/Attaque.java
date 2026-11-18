package com.mycompany.qualitedev.model;

/** Une attaque d'un Pokémon : un nom, un type et des dégâts de base. */
public record Attaque(String nom, TypePokemon type, int degats) {
}
