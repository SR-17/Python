# Fonction qui recupere les entrees de l utilisateur
# Elle fait appel a la fonction affichage()
# Cela permet aussi d avoir un controle total sur les entrees de l utilisateur
# Elle renvois ce que l utilisateur tape
def entree(valeur):
	valeur = affichage(valeur,0)
	variable = input();
	return variable
# Fonction qui calcule le modulo pour 
# permettre d identifier les multiples de 5
# Elle renvoit la valeur du modulo
def calcul_modulo(valeur):
	valeur = valeur % 5
	return valeur
# Fonction qui affiche du texte a l utilisateur
def affichage(parametre,somme):
	phrase = ''
	if(parametre == 1):
		phrase ='\nVeuillez entrer le premier nombre\n'
		print phrase
	elif parametre == 2:
		print '\n\nLa somme des multiples de 5 obtenue est',somme
	else:
		phrase = 'Veuillez entrer le deuxieme nombre\n'
		print phrase
	return phrase
# Fonction metier
# Elle gere le calcul de la somme
# Elle fait appel a la fonction :
# calcul_modulo() et affichage()
# Elle renvoit la somme obtenues
def calcul_somme(nombre_1,_nombre_2):
	modulo = 0
	somme = 0
	while nombre_2 >= nombre_1:
		modulo = calcul_modulo(nombre_1);
		if modulo == 0:
			somme = somme + nombre_1
			nombre_1 = nombre_1 + 1
		else:
			nombre_1 = nombre_1+1
	return somme
# Lancement du programme
if __name__ == '__main__':
# Recuperation des entrees utilisateurs
	nombre_1 = entree(1);
	nombre_2 = entree(3);
# Calcul de la somme
	somme = calcul_somme(nombre_1,nombre_2);
# Affichage de la somme
affichage(2,somme);
