'''
Created on 19.11.2012

@author: florian
@funktion: Dies ist der main-controller, welcher alle wichtigen Funktionen beinhaltet
'''

from model.policy import policy

def createPolicy(url,name,text):
        policy1 = policy(url, name, text)
        return policy1
    
def editPolicy(url,name,text):
        policy1 = policy(url, name, text)
        return policy1

if __name__ == '__main__':
    
# Objekt der Klasse commandLineHandler wird erstellt. 
# Schleife bis User Programm beendet
    # Dieser ueberprüft Kommmandozeilenparameter formal und gibt Typ der Anfrage und Parameter wie url etc. zurück
    # Anhand des übergebenen Typs wie die entsprechende Funktion mit den Paramtern ausgeführt