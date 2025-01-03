# 1. Crée le fichier myturtle.py avec l'importation de turtle
echo "import turtle as t" > myturtle.py

# 2. Transforme les commandes en instructions turtle et les ajouter à myturtle.py
cat turtle | sed 's/Tourne droite de \([0-9]*\).*/t.right(\1)/' | \
    sed 's/Tourne gauche de \([0-9]*\).*/t.left(\1)/' | \
    sed 's/Avance \([0-9]*\).*/t.forward(\1)/' | \
    sed 's/Recule \([0-9]*\).*/t.backward(\1)/'| 
# Exclusion de digest
    grep -v digest >> myturtle.py

# 3. Ajoute turtle.exitonclick() à la fin du fichier pour figer la fenêtre
echo "t.exitonclick()" >> myturtle.py

# 4. Exécute le script Python généré
python3 myturtle.py