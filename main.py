def afficher_menu():
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")

def main():
    taches = []
    
    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()
        
        if choix == "1":
            titre = input("Titre de la tâche : ").strip()
            if titre == "":
                print("Erreur : Le titre ne peut pas être vide.")
            else:
                taches.append(titre)
                print("Tâche ajoutée avec succès.")
                
        elif choix == "2":
            if not taches:
                print("La liste des tâches est vide.")
            else:
                print("\n--- LISTE DES TÂCHES ---")
                for i, t in enumerate(taches, 1):
                    print(f"{i}. {t}")
                    
        elif choix == "3":
            mot_cle = input("Entrez un mot-clé à rechercher : ").strip().lower()
            resultats = [t for t in taches if mot_cle in t.lower()]
            if not resultats:
                print("Aucune tâche trouvée.")
            else:
                print("\n--- RÉSULTATS DE RECHERCHE ---")
                for t in resultats:
                    print(f"- {t}")
                    
        elif choix == "0":
            print("Fermeture du programme. Au revoir !")
            break
        else:
            print("Option invalide, veuillez choisir entre 0 et 3.")

if __name__ == "__main__":
    main()