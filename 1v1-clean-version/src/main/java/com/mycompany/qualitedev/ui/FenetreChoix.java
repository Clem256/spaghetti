package com.mycompany.qualitedev.ui;

import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

/** Étape 1 : nom et image des deux Pokémon. */
public class FenetreChoix extends JFrame {

    private final JTextField nom1 = new JTextField(20);
    private final JTextField image1 = new JTextField(20);
    private final JTextField nom2 = new JTextField(20);
    private final JTextField image2 = new JTextField(20);

    public FenetreChoix() {
        super("Choix des Pokémon");
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        JPanel p = new JPanel(new GridBagLayout());
        ligne(p, 0, "Premier Pokémon", nom1, "Chemin image", image1);
        ligne(p, 1, "Second Pokémon", nom2, "Chemin image", image2);

        JButton valider = new JButton("Valider");
        valider.addActionListener(e -> valider());
        GridBagConstraints c = new GridBagConstraints();
        c.gridx = 0; c.gridy = 2; c.gridwidth = 4; c.insets = new Insets(10, 5, 5, 5);
        p.add(valider, c);

        setContentPane(p);
        pack();
        setLocationRelativeTo(null);
    }

    private static void ligne(JPanel p, int y, String lbl1, JTextField champ1, String lbl2, JTextField champ2) {
        GridBagConstraints c = new GridBagConstraints();
        c.gridy = y;
        c.insets = new Insets(5, 5, 5, 5);
        c.gridx = 0; p.add(new JLabel(lbl1), c);
        c.gridx = 1; p.add(champ1, c);
        c.gridx = 2; p.add(new JLabel(lbl2), c);
        c.gridx = 3; p.add(champ2, c);
    }

    private void valider() {
        new FenetreAttaques(
                nom1.getText().trim(), image1.getText().trim(),
                nom2.getText().trim(), image2.getText().trim()
        ).setVisible(true);
        dispose();
    }
}
