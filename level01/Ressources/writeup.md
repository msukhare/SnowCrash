En effectuant un cat/etc/passwd, les droits du flag01 attise notre curiosite.
En effet, au lieu de disposer d'un droit d'execution, soit x, on oobserve la chaine suivante: "42hDRfypTqqnw"

On va essayer differentes methodes d'encodage/d'encryption sur cette chaine pour trouver l'algorithme utilise (base64, cesar, etc..).

On testera ensuite l'algorithme de DES grace au programme hashcat permettant de tester differentes possibilites, en tombant sur ce post dans nos recherches "https://unix.stackexchange.com/questions/81240/manually-generate-password-for-etc-shadow".

Pour tester ces possibilites, on va lancer la commande suivante:

"./hashcat -a 3 -m 1500 string.txt  -o output.txt rockyou.txt"

"-a 3": choisit le type d'approche, soit du bruteforce dans notre cas..
"-m 1500 string.txt": choisit le type d'algorithme utilise, soit DES sur notre chaine stocke dans le fichier string.txt.
"rockyou.txt" est une liste de mots de passe les plus communs pour trouver la cle utilise dans notre eventuelle encryption DES.

On obtient alors le resultat "abcdefg", apres quelques minutes d'attente.

On utilise alors la commande "su flag01" avec notre mot de passe, puis getflag pour trouver le flag.
Pour acceder au niveau suivant: "su level02" avec notre flag en mot de passe.

