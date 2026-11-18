package com.mycompany.qualitedev.ui;

import com.mycompany.qualitedev.model.Attaque;
import com.mycompany.qualitedev.model.Pokemon;
import com.mycompany.qualitedev.model.TypePokemon;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.util.ArrayList;
import java.util.List;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSpinner;
import javax.swing.JTextField;
import javax.swing.SpinnerNumberModel;
import javax.swing.border.TitledBorder;

/** Formulaire d'un Pokémon : ses types et ses 4 attaques (nom, type, dégâts). */
class PanneauPokemon extends JPanel {

    private static final int NB_ATTAQUES = 4;

    private final String nom;
    private final String cheminImage;
    private final JComboBox<TypePokemon> type1 = new JComboBox<>(TypePokemon.values());
    private final JComboBox<TypePokemon> type2 = new JComboBox<>();
    private final JTextField[] nomsAttaques = new JTextField[NB_ATTAQUES];
    private final JComboBox<TypePokemon>[] typesAttaques = newTableauCombos();
    private final JSpinner[] degatsAttaques = new JSpinner[NB_ATTAQUES];

    PanneauPokemon(String nom, String cheminImage) {
        this.nom = nom;
        this.cheminImage = cheminImage;
        setLayout(new GridBagLayout());
        setBorder(new TitledBorder(nom));

        type2.addItem(null); // 2e type facultatif
        for (TypePokemon t : TypePokemon.values()) type2.addItem(t);

        GridBagConstraints c = new GridBagConstraints();
        c.insets = new Insets(3, 5, 3, 5);
        c.anchor = GridBagConstraints.WEST;

        c.gridy = 0; c.gridx = 0; add(new JLabel("Type 1"), c);
        c.gridx = 1; add(type1, c);
        c.gridy = 1; c.gridx = 0; add(new JLabel("Type 2"), c);
        c.gridx = 1; add(type2, c);

        c.gridy = 2; c.gridx = 0; add(new JLabel("Attaque"), c);
        c.gridx = 1; add(new JLabel("Type"), c);
        c.gridx = 2; add(new JLabel("Dégâts"), c);

        for (int i = 0; i < NB_ATTAQUES; i++) {
            nomsAttaques[i] = new JTextField(12);
            typesAttaques[i] = new JComboBox<>(TypePokemon.values());
            degatsAttaques[i] = new JSpinner(new SpinnerNumberModel(40, 0, 999, 5));
            c.gridy = 3 + i;
            c.gridx = 0; add(nomsAttaques[i], c);
            c.gridx = 1; add(typesAttaques[i], c);
            c.gridx = 2; add(degatsAttaques[i], c);
        }
    }

    @SuppressWarnings("unchecked")
    private static JComboBox<TypePokemon>[] newTableauCombos() {
        return new JComboBox[NB_ATTAQUES];
    }

    /** Construit le Pokémon à partir de ce qui est saisi ; les attaques sans nom sont ignorées. */
    Pokemon creerPokemon() {
        List<Attaque> attaques = new ArrayList<>();
        for (int i = 0; i < NB_ATTAQUES; i++) {
            String nomAttaque = nomsAttaques[i].getText().trim();
            if (nomAttaque.isEmpty()) continue;
            attaques.add(new Attaque(
                    nomAttaque,
                    (TypePokemon) typesAttaques[i].getSelectedItem(),
                    (Integer) degatsAttaques[i].getValue()));
        }
        return new Pokemon(nom, (TypePokemon) type1.getSelectedItem(),
                (TypePokemon) type2.getSelectedItem(), cheminImage, attaques);
    }
}
