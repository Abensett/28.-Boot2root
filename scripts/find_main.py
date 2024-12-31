#!/usr/bin/env python3
import os
import sys

# Vérification du répertoire passé en argument
if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
    print("Usage: python script.py <chemin_du_répertoire>")
    sys.exit(1)

# Parcours des fichiers et traitement
for filename in os.listdir(sys.argv[1]):
    file_path = os.path.join(sys.argv[1], filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            if "main()" in content:
                print(f"Le fichier '{filename}' contient 'main'.")
