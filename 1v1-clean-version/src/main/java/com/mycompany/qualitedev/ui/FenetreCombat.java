package com.mycompany.qualitedev.ui;

import com.mycompany.qualitedev.model.Attaque;
import com.mycompany.qualitedev.model.Pokemon;
import java.awt.GridLayout;
import javax.swing.BoxLayout;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;

/** Étape 3 : écran du combat 1v1 (pour l'instant, affichage seulement). */
public class FenetreCombat extends JFrame {

    public FenetreCombat(Pokemon p1, Pokemon p2) {
        super("Combat Pokémon 1v1");
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        JPanel racine = new JPanel(new GridLayout(1, 2, 20, 0));
        racine.add(creerColonne(p1));
        racine.add(creerColonne(p2));

        setContentPane(racine);
        pack();
        setLocationRelativeTo(null);
    }

    private JPanel creerColonne(Pokemon pokemon) {
        JPanel colonne = new JPanel();
        colonne.setLayout(new BoxLayout(colonne, BoxLayout.Y_AXIS));

        colonne.add(centre(new JLabel(pokemon.getNom() + "   PV : " + pokemon.getPv() + "/" + pokemon.getPvMax())));
        colonne.add(centre(new JLabel(new ImageIcon(pokemon.getCheminImage()), SwingConstants.CENTER)));
        for (Attaque a : pokemon.getAttaques()) {
            colonne.add(centre(new JButton(a.nom() + " (" + a.type() + ") - " + a.degats())));
        }
        return colonne;
    }

    private static <T extends JComponent> T centre(T composant) {
        composant.setAlignmentX(CENTER_ALIGNMENT);
        return composant;
    }
}
