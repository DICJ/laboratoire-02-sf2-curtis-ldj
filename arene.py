from personnage import Personnage
import random

class Arene : 
    def __init__(self ):

        self.__lst_personnages = []

    @property

    def lst_personnages (self) -> list : 

        return self.__lst_personnages

    def ajouter_personnages(self , personnage : Personnage) :
     
      self.__lst_personnages.append(personnage)

    def afficher_personnages(self , personnage ) :
      
      for personnage in self.__lst_personnages :
         print (f" {personnage.nom} : {personnage.str}")   
    def combat_de_personnage (perso_1 : Personnage , perso_2 : Personnage ) : 
       
       print ("---- DEBUT DU GRAND COMBAT  ----")
       
       while perso_1.vie > 0 and perso_2.vie > 0 :
          
          degats = perso_1.attaquer()

          perso_2.subir_degat(degats)

          print(f"{perso_1.nom} inflige {degats } au {perso_2.nom}")

          if perso_2.vie <= 0 :
              
              break
          
          degats = perso_2.attaquer()

          perso_1.subir_degat(degats)

          print(f"{perso_2.nom} inflige {degats } au {perso_1.nom}")

          if  perso_1.vie <= 0 :
              
              break
       if perso_1.vie > 0 :
          
          print(f"le vainceur est {perso_1.nom}") 
          return perso_1
       else : 
          print(f"le vainceur est {perso_2.nom}")
          return perso_2
            
    def soigner_personnage(self, numero):

     

      if 0 <= numero < len(self._lst_personnages):

          self._lst_personnages[numero].reset()

          print(f"{self._lst_personnages[numero].nom} a été soigné!")

      else:

          print("numero inconnu")
 
    def nettoyer_arene(self):

      """Supprime tous les personnages qui sont  morts"""

      vivants = [p for p in self._lst_personnages if p.vie > 0]

      morts = len(self._lst_personnages) - len(vivants)

      self._lst_personnages = vivants

      print(f" le nombre de {morts} ")

    def lancer_battle_royal(self):

      """Bataille jusqu'à ce qu'il reste un seul combattant"""

      if len(self._lst_personnages) < 2:

          print("Pas assez de combattants")

          return

      # je soigne avant de commencer

      for p in self._lst_personnages:

          p.reset()

      
      print("BATTLE ROYAL COMMENCE!")

     
      while len(self._lst_personnages) > 1:

          print(f"\n{len(self._lst_personnages)} combattants restants")

          # detyermine des combattants au hasard 
         

          i1 = random.randint(0, len(self._lst_personnages) - 1)

          i2 = random.randint(0, len(self._lst_personnages) - 1)

          while i1 == i2:  # Évite le même numero

              i2 = random.randint(0, len(self._lst_personnages) - 1)

          p1 = self._lst_personnages[i1]

          p2 = self._lst_personnages[i2]

          print(f"\nCombat: {p1.nom} vs {p2.nom}")

          vainqueur = self.combat_de_personnage(p1, p2)

          vainqueur.reset()
        
          self.nettoyer_arene()

      print(" FIN DU BATTLE ROYAL ")

      print(f"Le grand vainqueur est: {self._lst_personnages[0]}")

      
 