# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 23:02:56 2021

@author: Nico
"""

class spill:
    def __init__(self,spørsmål,alternativ,svar):
        self.spørsmål = spørsmål
        self.alternativ = alternativ
        self.svar = svar
        
    def __str__(self):
        spørsmål = f"""{self.spørsmål}
        1. {self.alternativ[0]}
        2. {self.alternativ[1]}
        3. {self.alternativ[2]}"""
        return spørsmål
    
    def sjekk_svar(self, svaret):
        if str(self.svar) == str(svaret):
            print("Svaret ditt er riktig")
        else:
            print("Svaret ditt er feil")
            
if __name__ == "__main__":
    spørsmål = "Hvilket pc-merke har jeg?"
    alternativ = ["Acer", "Lenovo", "Asus"]
    svar = 2
    
    klassen = spill(spørsmål, alternativ, svar)
    print((klassen))
    svaret = input("Svar: ")
    klassen.sjekk_svar(svaret)  
    
    spørsmål = "Hva er best?"
    alternativ = ["Cola_zero", "Fanta", "Pepsi_max"]
    svar = 3
    
    
    klassen = spill(spørsmål, alternativ, svar)
    print(klassen)
    svaret = input("Svar: ")
    klassen.sjekk_svar(svaret)
    
    
    