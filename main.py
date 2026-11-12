import json

def sauvegarder_contacts():
   with open("contacts.json", "w", encoding="utf-8") as fichier:
      json.dump(contacts, fichier, indent=4, ensure_ascii=False)

def charger_contacts():
   try:
      with open("contacts.json", "r", encoding="utf-8") as fichier:
         return json.load(fichier)
   except (FileNotFoundError, json.JSONDecodeError):
      return []
   
print("=== GESTIONNAIRE DE CONTACTS ===")

contacts = charger_contacts()

while True:
 print("Bienvenue dans votre répertoire !")
 print("1. Ajoutez un contact")
 print("2. Afficher les contacts")
 print("3. Rechercher un contact")
 print("4. Modifier un contact")
 print("5. Supprimer un contact")
 print("6. Quitter")

 choix = input("Choisisser une option (1-6) : ")

 if choix == "1":
    print("Vous avez choisi d'ajouter un contact.")
    nom = input("Nom du contact : ")
    telephone = input("Numéro de télephone : ")
    email = input("Adresse e-mail : ")

    contact = {
       "nom": nom,
       "telephone": telephone,
       "email": email
    }

    contacts.append(contact)
    sauvegarder_contacts()
    print("Contact ajoutez avec succès !")

 elif choix == "2":
    print("Vous avez choisi d'afficher les contacts.")
    if not contacts:
       print("Votre répertoire est vide.")
    else:
       for contact in contacts:
          print("Nom :", contact["nom"])
          print("Télephone :", contact["telephone"])
          print("E-mail :", contact["email"])
          print("--------------------")

 elif choix == "3":
    print("Vous avez choisi de rechercher un contact.")
    recherche = input("Nom du contact à rechercher : ")
    trouve = False

    for contact in contacts:
       if contact["nom"].lower() == recherche.lower():
          print("Contact trouvé !")
          print("Nom :", contact["nom"])
          print("Téléphone :", contact["telephone"])
          print("E-mail :", contact["email"])
          trouve = True
    if not trouve:
       print("Aucun contact trouvé.")

 elif choix == "4":
    print("Vous avez choisi de modifier un contact.")
    recherche = input("Nom du contact à modifier : ")
    trouve = False

    for contact in contacts:
       if contact["nom"].lower() == recherche.lower():
          print("Contact trouvé :", contact["nom"])

          nouveau_telephone = input("Nouveau téléphone : ")
          nouvel_email = input("Nouvel e-mail : ")

          contact["telephone"] = nouveau_telephone
          contact["email"] = nouvel_email
          sauvegarder_contacts()
          trouve = True
          print("Contatct modifié avec succès !")
          break 
    if not trouve:
       print("Aucun contact trouvé.")

 elif choix == "5":
    print("Vous avez choisi de supprimer un contact.")
    recherche = input("Nom du contact à supprimer : ")
    trouve = False

    for contact in contacts:
       if contact["nom"].lower() == recherche.lower():
          contacts.remove(contact)
          sauvegarder_contacts()
          trouve = True
          print("contact supprimé avec succès !")
          break
    if not trouve:
      print("Aucun contact trouvé.")

 elif choix == "6":
    print("Au revoir et à bientôt !")
    break
 else:
    print("Erreur : veuillez choisir une option entre 1 et 6.")
 