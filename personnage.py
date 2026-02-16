import random

class Personnage : 
    """la classe personnage represente un combattant general 
    """
    def __init__(self ,  nom : str , vie : int , attaque : int ) :

        self.__nom = nom 
        self.__vie = vie
        self.__attaque = attaque
        self._vie_max = vie  
        self._armure = None 

    @property
    def nom(self) -> None : 
        return self.__nom
    
    @nom.setter 
    def nom(self , nouveau_nom) -> None :
        self.__nom = nouveau_nom 

    @property
    def vie(self ) ->  int :
         return self.__vie
    @vie.setter 
    def vie(self , nouvelle_vie ) -> int :
        if 0 < nouvelle_vie < 500 :
           self.__vie = nouvelle_vie
        else :
            self.__vie = 1
 
    @property
    
    def attaque(self ) ->  int :
         return self.__attaque
    
    @attaque.setter 
    def attaque(self , nouvelle_attaque ) -> int :
        if 0 < nouvelle_attaque < 50 :
           self.__attaque = nouvelle_attaque
        else :
            self.__attaque = 1

    @property

    def vie_max(self):
       
       return self._vie_max
    
    def reset(self):
   
      self._vie = self._vie_max
    
    def __str__(self) : 
        return f" NOM DU PERSO : {self.nom } - VIE : {self.vie} - ATTAQUE : {self.attaque} "
    
    def subir_degat(self , degat : int ) -> int :
        self.vie -= degat
        if self.vie < 0 :
            self.vie = 0

class Guerrier (Personnage) :

    """La classe Guerrier est un Personnage qui est plus résistant
    """
    def __init__(self, nom, vie, attaque , force : int):
        super().__init__(nom, vie, attaque)
        self.__force = force 

    @property
    def force(self ) ->  int :
         return self.__force
    
    @force.setter 
    def force(self , nouvelle_force ) -> int :
        if 1 < nouvelle_force < 50 :
           self.__force = nouvelle_force
        else :
            self.__force = 1

    def __str__(self)  : 
        return f" GUERRIER : {self.nom } - VIE  : {self.vie} - ATTAQUE : {self.attaque} - FORCE : {self.force} "
    
    def attaquer(self) -> int: 
        degats =  self.attaque + (self.force / 2) + random.randint(-2 , 2)
        return degats
    
class Mage(Personnage) : 
    """La classe Mage est un Personnage qui attaque avec du mana
    """
    def __init__(self, nom, vie, attaque ,  mana : int):
        super().__init__(nom, vie, attaque)
        self.__mana = mana
        self._mana_max = mana
    @property
    def mana(self ) ->  int :
         return self.__mana
    
    @mana.setter 
    def mana(self , nouveau_mana ) -> int :
        if 0 < nouveau_mana < 100 :
           self.__mana = nouveau_mana
        else :
            self.__mana = 1

    def __str__(self)  : 
        return f" MAGE : {self.nom } - VIE  : {self.vie} - ATTAQUE : {self.attaque} - MANA  : {self.mana}"
    
    def attaquer(self) -> int: 

        if self.mana > 1 : 
          self.mana -= random.randint(15 , 25)
          return self.attaque + 60
        else : 
            return 3 

class Archer (Personnage ) : 

    def __init__(self, nom, vie, attaque , dexterite : int ):

        super().__init__(nom, vie, attaque )

        self.__dexterite =  dexterite 

    @property
    def dexterite(self ) ->  int :
         return self.__dexterite
    
    @dexterite.setter 

    def dexterite(self , nouvelle_dexterite ) -> int :
        if 40 < self.__dexterite < 70 :
           self.__dexterite = nouvelle_dexterite
        else :
            self.__dexterite = 50

    def __str__(self)  : 
        return f" ARCHER : {self.nom } - VIE  : {self.vie} - ATTAQUE : {self.attaque} - DEXTERITE : {self.dexterite} "
    
    def attaquer(self) -> int: 
        nombre =  self.randint(0 , 100) 
        if nombre < self.dexterite : 
           degats *= 2  
        else : 
            degats = self.attaque + 15  

class Soldat(Personnage):
   
   def __init__(self, nom, vie, attaque, armure):
       
       super().__init__(nom, vie, attaque)

       self._armure = armure  
   @property
   def armure(self):
       return self._armure
   

   def __str__(self):
       
       return f"SOLDAT : {self.nom} - VIE : {self.vie} - ATTAQUE : {self.attaque} - ARMURE : {self.armure}"
   def attaquer(self):
       
       
       return self.attaque + random.randint(-2, 2)
   def subir_degat(self, degat):
       
       degat_reduit = max(0, degat - self.armure // 2)

       super().subir_degat(degat_reduit)            