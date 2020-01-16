Ayant affaire a un fichier lua, il nous est possible de lire son contenu.

On voit qu'on a  affaire un script de serveur qui tourne en continu.
Il nous sera possible de se connecter a ce serveur avec la commande "nc",
car nous connaissons son ip, ainsi que son port, grace a la lecture du contenu de ce script.

On se rend egalement compte alors qu'une requete va s'effectuer au moment ou l'on va taper notre mot de passe,
pour se connecter.

On va tenter de lancer la commande getflag par le biais de ce script,
car nous en possedons pas les droits pour al lancer.

Il suffit alors de lancer les commandes suivantes:

"nc 127.0.0.1 5151" pour se connecter au serveur.

Puis, au moment de selectionner un mot de passe:

"`getflag > /tmp/test`" qui va lancer notre commande getflag dans un sous-terminal
et stocker son resultat dans le fichier test dans le dossier /tmp.

Un "cat /tmp/test" nous donne alors le flag que l'on recherche
