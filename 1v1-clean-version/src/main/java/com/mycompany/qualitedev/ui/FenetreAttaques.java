package com.mycompany.qualitedev.ui;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

/** Étape 2 : types et attaques des deux Pokémon. */
public class FenetreAttaques extends JFrame {

    private final PanneauPokemon panneau1;
    private final PanneauPokemon panneau2;

    public FenetreAttaques(String nom1, String image1, String nom2, String image2) {
        super("Informations complémentaires");
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        panneau1 = new PanneauPokemon(nom1, image1);
        panneau2 = new PanneauPokemon(nom2, image2);

        JPanel formulaires = new JPanel(new GridLayout(1, 2));
        formulaires.add(panneau1);
        formulaires.add(panneau2);

        JButton valider = new JButton("Valider");
        valider.addActionListener(e -> lancerCombat());

        JPanel racine = new JPanel(new BorderLayout());
        racine.add(formulaires, BorderLayout.CENTER);
        racine.add(valider, BorderLayout.SOUTH);

        setContentPane(racine);
        pack();
        setLocationRelativeTo(null);
    }

    private void lancerCombat() {
        new FenetreCombat(panneau1.creerPokemon(), panneau2.creerPokemon()).setVisible(true);
        dispose();
    }
}
