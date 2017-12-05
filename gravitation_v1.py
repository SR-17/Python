# Fonction qui sert à calculer

def calcul_moi(m1,m2,x,constante_gravitation):
	resultat = constante_gravitation * (m1*m2)/(x)**2
	return resultat
# Fonction qui recupere les valeurs de l utilisateur
def donne_moi():
	x = int(input('Quel valeur 1 ?'))
	x_voulu = int(input('Quel valeur 2 ?'))
	return x,x_voulu
# Fonction qui boucle tant qu on a pas ce qu on recherche
# cest a dire la valeur de x_voulu
def boucle(x,x_voulu,m1,m2,constante_gravitation):
	while x < x_voulu:
		resultat = calcul_moi(m1,m2,x,constante_gravitation);
		print('F de ', x , 'fait ', resultat)
		x = x*2
# Directive de debut
if __name__ == '__main__':
	m1,m2 = 10000,10000
	constante_gravitation = 6.67*10**-11
	x,x_voulu = donne_moi();
	boucle(x,x_voulu,m1,m2,constante_gravitation);
	
