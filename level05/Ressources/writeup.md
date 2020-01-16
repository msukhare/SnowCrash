Dans un premier temps, nous allons lister les fichiers en liens avec l'utilisateur "flag05" avec la commande:

"find / -user flag05"

On peut alors voir un seul fichier dont l'acces nous est autorise, soit:

"/usr/sbin/openarenaserver"

En lisant ce fichier avec cat, on se rend compte que c'est un script qui va lire dans les fichiers presents 
dans le dossier "/opt/openarenaserver/", puis executer les commandes que ces memes fichiers peuvent contenir.

On pourra alors executer une commande, comme getflag par exemple.
Cependant, l'acces nous est interdit.

En se connectant au serveur ssh, on a ete accuellit par le message suivant "A mail has been sent"
En fouillant dans les variables de mail, avec la commande: "cat /var/mail/$USER"

On peut voir qu'un cron est mis en place pour executer notre script dont nous ne possedons pas les droits pour l'executer.
Mais cron peut l'executer, par contre, et ce, toutes les deux minutes.

Il suffit alors de creer un script dans le dossier "/opt/openarenaserver/", nomme test par exemple, ayant pour contenu:

"/bin/getflag > /tmp/flag05" afin de pouvoir lire le resultat de notre commande dans un fichier temporaire.

On ajoute ensuite les droit d'execution a notre script avec la commande:

"chmod +x /opt/openarenaserver/test"

On attend 2 minutes, et on peut alors lire dans notre fichier tmp/flag05 le flag de ce nouveau.
