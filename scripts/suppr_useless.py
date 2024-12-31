#!/usr/bin/env python3
import sys

# Vérification que l'argument du fichier est fourni
if len(sys.argv) != 2:
    print("Usage: python script.py <chemin_du_fichier>")
    sys.exit(1)

# Récupération du fichier passé en argument
file_path = sys.argv[1]

# Vérification que le fichier existe
try:
    with open(file_path, 'r') as infile:
        lines = infile.readlines()
except FileNotFoundError:
    print(f"Erreur : Le fichier '{file_path}' n'existe pas.")
    sys.exit(1)

# Filtrer les lignes qui ne contiennent pas 'useless'
filtered_lines = [line for line in lines if '//' and 'hahaha' not in line]

# Réécriture du fichier avec les lignes filtrées
with open(file_path, 'w') as outfile:
    outfile.writelines(filtered_lines)

print(f"Les lignes contenant 'useless' ont été supprimées de '{file_path}'.")