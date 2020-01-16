Pour commencer, nous allons chercher tout les fichiers appartenant a l'utilisateur flag00 avec la commande:

"find / -user flag00"

On va alors trouver deux fichiers dont l'acces nous est permi.
"/usr/sbin/john"
"/rofs/usr/sbin/john"

En les inspectant avec la commande cat, on trouve le contenu suivant: "cdiiddwpgswtgt", ne correspondant a aucun hash connu.
On a surement affaire a un chiffrement de cesar.

En testant toutes les possibilites sur le site: "https://www.dcode.fr/chiffre-cesar"
On trouve alors le code "nottoohardhere" avec un decalage additif de 15.

On utilise alors la commande "su flag00" avec notre mot de passe, puis getflag pour trouver le flag.
Pour acceder au niveau suivant: "su level01" avec notre flag en mot de passe.

