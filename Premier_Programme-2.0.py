# Cette fonction est utilitaire. Cest à dire quelle va afficher le nombre de hello world que
# l'on veut.
def coucou_le_monde(nbr_de_tour):
	while i<nbr_de_tour:
		print("Hello world !");
		i = i+1;
# Cette fonction demande a lutilisateur combien de fois il souhaite que le message sois repeté.
def combien():
	nbr_boucle = input("Combien de fois on affiche hello world");
	nbr_boucle = nbr_boucle+1;
# Directive d'initiation : Annonce à python que le programme démarre la. 
#On appel la fonction métier(coucou_le_monde) 
#et la fonction input(combien) pour lancer le programme tout simplement.
if __name__ == '__main__':
	coucou_le_monde(combien());
	
