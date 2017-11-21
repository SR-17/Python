# Fonction qui est considerer comme la fonction metier             
# Elle ne fait que retourner le resultat a la fonction dialogue    

def calcul_imc(taille,masse):
        taille = taille*taille
        imc = masse / taille
        return imc

# Fonction qui recupere la taille et le poids. Elle est consideree comme la fonction input

def demande_info():
        taille = input("En attente de votre taille en cm ...\n>>> ");
        masse = input("En attente de votre poids ...\n>>> ");
        masse = int(masse)
        taille = float(taille)
        return taille,masse;

# Fonction qui ne fait que appeler les fonctions nécessaires au programme puis affiche les resultats quand nécessaire. C'est la fonction output.
def dialogue():
        print("Bienvenue dans le calculateur IMC")
        taille,masse = demande_info();
        print("Vous mesurez ",taille, "\n vous peser",masse)
        print("Calcul de votre imc...")
        imc = calcul_imc(taille,masse);
        print("Votre IMC est de ",imc)
        print("\nRappel de vos valeurs :","\n Taille : ",taille,"\nPoids : ",masse)
        
# Directive qui annonce à python que le programme démarre ici
if __name__ == '__main__':
        dialogue();
