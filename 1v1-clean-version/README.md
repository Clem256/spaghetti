# Qualitedev – mini showdown Pokémon

Petite appli Swing : on choisit deux Pokémon (nom + image), on saisit leurs types et 4 attaques chacun, puis un écran de combat 1v1 s'affiche.

## Lancer
```
mvn compile exec:java -Dexec.mainClass=com.mycompany.qualitedev.Main
```
(ou lancer `Main` depuis l'IDE, à la racine du projet pour que `images/...` soit trouvé)

## Structure
- `model/` : logique pure, sans Swing — `TypePokemon` (tableau d'efficacité), `Pokemon`, `Attaque`
- `ui/` : les 3 fenêtres — `FenetreChoix` → `FenetreAttaques` (+ `PanneauPokemon`) → `FenetreCombat`
- `images/` : images d'exemple (ex. `images/cat.png`)

## Reste à faire
Les boutons d'attaque de `FenetreCombat` ne font rien : brancher `Pokemon.recevoir(attaque)`, gérer les tours (stat `speed`) et l'état KO.
