#!/usr/bin/env python3
import os
import sys
import re

# Vérification que les arguments sont fournis
if len(sys.argv) != 3:
    print("Usage: python script.py <chemin_du_répertoire> <fichier_sortie>")
    sys.exit(1)

# Récupération des arguments
directory_path = sys.argv[1]
output_file = sys.argv[2]

# Vérification que le répertoire existe
if not os.path.isdir(directory_path):
    print(f"Erreur : Le répertoire '{directory_path}' n'existe pas.")
    sys.exit(1)

# Fonction pour extraire le numéro du commentaire dans chaque fichier
def extract_number(file_path):
    """Extrait le numéro du commentaire sous la forme `//file<number>`"""
    with open(file_path, 'r') as file:
        # Recherche d'un commentaire avec le format //file<number>
        for line in file:
            match = re.match(r'//file(\d+)', line)
            if match:
                return int(match.group(1))  # Retourne le numéro comme un entier
    return float('inf')  # Si aucun numéro n'est trouvé, le fichier sera mis à la fin

# Liste des fichiers dans le répertoire, triée par le numéro dans le commentaire
files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
files_with_numbers = []

# Extraire les numéros et les associer aux fichiers
for filename in files:
    file_path = os.path.join(directory_path, filename)
    number = extract_number(file_path)
    files_with_numbers.append((file_path, number))

# Trier les fichiers par numéro (ordre croissant)
files_with_numbers.sort(key=lambda x: x[1])

# Ouverture du fichier de sortie en mode écriture
with open(output_file, 'w') as outfile:
    # Parcours des fichiers triés par numéro
    for file_path, _ in files_with_numbers:
        print(f"Ajout du fichier : {file_path}")
        with open(file_path, 'r') as infile:
            content = infile.read()
            outfile.write(content + "\n")  # Ajoute un saut de ligne après chaque fichier

print(f"Tous les fichiers ont été concaténés dans '{output_file}'.")
