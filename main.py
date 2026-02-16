from personnage import Personnage , Guerrier , Mage , Archer 
from arene import Arene
from armure import Armure
import random 



def afficher_menu():
    
    print("Menu:")
    print("1. ajouter un personnage ")
    print("2. voir les personnages dans larene ")
    print("3. Faire combattre deux personnages ")
    print("4. gerer larene ")
    print("5. Nombre de combattants ")
    print("6. soigner un personnage ")
    print("7. nettoyer larene ( enlever les mports) ")
    print("0. Quitter ")


#début du programme
choix = 10000

while choix != 0:
    afficher_menu()
    arene = Arene ()
   
    choix = int(input("Entrez un nombre (0 pour quitter): "))

    match choix:
        case 1:    
            print (" --- AJOUT DE PERSONNAGE ---")
            print(" les types disponibles : Guerrier, Mage, Archer , Soldat") 
            print()

            type_perso = input("Type :  ").strip().lower()

            nom = input("Nom : ").strip().lower()

            vie = int(input("Points de vie : "))

            attaque = int(input("Attaque de base : "))

            print("Veux-tu ajouter une armure :: oui ou non ")

            armure_choisie = None

            if input().lower() == "oui ":

                nom_armure = input("Nom de l'armure : ")

                points = int(input("Points d'armure (0-15) : "))

                armure_choisie = Armure(nom_armure, points)


            if type_perso.strip().lower() == "guerrier":

                force = int(input("Force (1-50) : "))
    
                perso = Guerrier(nom, vie, attaque, force)

            elif type_perso.lower() == "mage":
                   
                 mana = int(input("Mana (1-100) : "))

                 perso = Mage(nom, vie, attaque, mana)

            elif type_perso.lower() == "archer":
                   
                 dexterite = int(input("Dextérité (40-70) : "))

                 perso = Archer(nom, vie, attaque, dexterite)
            elif type_perso == "soldat":
             # Le soldat DOIT avoir une armure
               if not armure_choisie:

                print(" Le soldat doit avoir une armure!")

               armure_choisie = Armure("Armure par defaut du soldat", 10)
     
            else:
                   print("ce type de personnage ne peut etre identifie  !")

                   continue
    
            arene.ajouter_personnages(perso)

            print(f"--- {nom} est present dans larene --- ")


      
        case 2:
            print (" --- VOIR LES  PERSONNAGES ---")
            if not arene.lst_personnages :
                print ("Larene est vide ")
            else : 
                for i , personnage in enumerate(arene.lst_personnages) :
                  print (f" {i} { personnage }")    
         
        case 3:
            print ("---- COMBAT DE PERSO ----")
            if len(arene.lst_personnages) < 2 :

                print(" il ya pas assez de combattants il en faut minimum 2 ")
                continue 
           
            for i, p in enumerate(arene.lst_personnages):
                   
                   print(f"{i} --- {p.nom}")

            try:

              i1 = int(input("choisi le numero  du 1er combattant : "))
              i2 = int(input("choisi le numero du 2eme  combattant : "))
              if i1 >= len(arene.lst_personnages) or i2 >= len(arene.lst_personnages):
                print("Impossible ")
                continue
              if i1 == i2:
                print("Un personnage ne peut pas se battre contre lui-même !")
                continue
              
            # le combat

              p1 = arene.lst_personnages[i1]
              p2 = arene.lst_personnages[i2]
              vainqueur = arene.combat_de_personnage(p1, p2)
              print(f"\nLE VAINQUEUR EST : ---{vainqueur.nom}--- ")

            except ValueError:
            
              print("entre des nombres coherents ")
            
            
            pass
        case 4:
            print("\n--- le NETTOYAGE ---")

            confirmation = input("vous voulez vraiment vider larene oui/ non  : ")

            if confirmation.strip().lower() == "oui":
                   
                   arene.lst_personnages = []

                   print("larene est effictivement vide ")
            else:
                   print("Annulé")
            
            
        case 5 :

            print(f"\n le  Nombre de combattants : {len(arene.lst_personnages)}")
     
        case 6 :

            numero = int(input("numero  du personnage a soigner: "))

            arene.soigner_personnage(numero)

        case 7 :

            arene.lancer_battle_royal()

        case 8 : 

            arene.nettoyer_arene()
       