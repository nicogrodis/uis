# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 08:47:32 2021

@author: Nico
"""
class spill:
    def __init__(self,spørsmål,korrekt_svar,alternativ):
        self.spørsmål = spørsmål
        self.korrekt_svar = korrekt_svar
        self.alternativ = alternativ
           
        
        
    def __str__(self):
        spørsmål = f"{self.spørsmål} \n"
        for alt in range(len(self.alternativ)):
            spørsmål += f"{alt}.{self.alternativ[alt]}\n"
        
        return "\n" + spørsmål
    

    def sjekk_svar(self, svar1, svar2): 
        if str(self.korrekt_svar[0][1]) == str(svar1):
            print("Spiller 1: Riktig")     
        else: 
            print ("Spiller 1: Feil")
        if str(self.korrekt_svar[0][1]) == str(svar2):
            print("Spiller 2: Riktig")
            print("\n")
        else: 
            print ("Spiller 2: Feil")
            print("\n")
        print("Riktig svar er: " + self.korrekt_svar[0][1])
        return (str(self.korrekt_svar[0][1]) == str(svar1),str(self.korrekt_svar[0][1]) == str(svar2))

        


def filleser():
   spørsmålliste = []
   with open("123.txt", "r", encoding="UTF-8") as file:
          for line in file:
           split = line.split(":")
           spørsmål = split[0]
           korrekt_svar = split[1].split(": ")
           alternativ = split[2].strip("[] \n").split(",")        
           spørsmålliste.append(spill(spørsmål, korrekt_svar, alternativ))                                           
          return spørsmålliste
        

        
        
if __name__ == "__main__":        
    filleser = filleser()  
 
score1 = 0
score2 = 0


for spm in filleser:
    print(spm)
    svar1 = int(input("Spiller1 avgi svar: "))
    svar2 = int(input("Spiller2 avgi svar: "))
    print("\n")
    #spm.sjekk_svar(svar1, svar2)
    p1r, p2r = spm.sjekk_svar(svar1, svar2)
    if p1r:
        score1 +=1
    if p2r:
        score2 +=1
    print("\n")    
    print(f"Stillingen til nå er:\n Spiller1: {score1}\n Spiller2: {score2}")
            
    
    
    
   
        


  
   





