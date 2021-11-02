# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 08:47:32 2021

@author: Nico
"""
score = 0

class spill:
    def __init__(self,spørsmål,korrekt_svar,alternativ):
        self.spørsmål = spørsmål
        self.korrekt_svar = korrekt_svar
        self.alternativ = alternativ
           
        
        
    def __str__(self):
        spørsmål = f"""{self.spørsmål}
        1. {self.alternativ[0]}
        2. {self.alternativ[1]}
        3. {self.alternativ[2]}
        4. {self.alternativ[3]}
        5. {self.alternativ[3]}"""
        return spørsmål
    

    def sjekk_svar(self, svar1, svar2):
        if str(self.korrekt_svar[0][1]) == str(svar1):
            print("Spiller 1: Riktig")
            
        else: 
            print ("Spiller 1: Feil")
        if str(self.korrekt_svar[0][1]) == str(svar2):
            print("Spiller 2: Riktig")

        else: 
            print ("Spiller 2: Feil")


def filleser():
   spørsmålliste = []
   with open("sporsmaal.txt", "r", encoding="UTF-8") as file:
          for line in file:
           split = line.split(":")
           spørsmål = split[0]
           korrekt_svar = split[1].split(": ")
           alternativ = split[2].split(",")        
           spørsmålliste.append(spill(spørsmål, korrekt_svar, alternativ))                                           
          return spørsmålliste
        

        
        
if __name__ == "__main__":        
    filleser = filleser()
    
                
for spm in filleser:
    print(spm)
    svar1 = int(input("Spiller1 avgi svar: "))
    svar2 = int(input("Spiller2 avgi svar: "))
    spm.sjekk_svar(svar1, svar2)
    

    
    
    
   
        


  
   





