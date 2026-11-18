package com.mycompany.qualitedev;

import com.mycompany.qualitedev.ui.FenetreChoix;
import javax.swing.SwingUtilities;

/** Point d'entrée : ouvre la première fenêtre (choix des deux Pokémon). */
public class Main {

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new FenetreChoix().setVisible(true));
    }
}
