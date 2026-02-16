class Armure:
   def __init__(self, nom, points_armure):
       
       self._nom = nom
       self._points_armure = max(0, min(15, points_armure))  # Entre 0 et 15

   @property
   def nom(self):
       return self._nom
   
   @property
   def points_armure(self):
       return self._points_armure
   
   def __str__(self):
       
       return f"{self._nom} ({self._points_armure} pts)"