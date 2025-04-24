import os
import io

# --- Fonction loads lasts names return all the names in a text document---
def load_users():
    with open("users.txt", "r") as file:
        return [line.strip() for line in file.readlines()]
    return []

# --- Fonction save name write a name in a texte doc and add a return ---
def save_user(nom):
    with io.open("users.txt", "rb") as fichier:
        fichier.write(nom)
