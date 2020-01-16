On a dans notre dossier un fichier se terminant par un .pcap.
Il s'agit d'une capture reseau. On va donc avoir besoin d'un logiciel nomme wireshark pour l'analyser.

On telecharge le fichier .pcap avec la commande:
"scp -P 4242 level00@10.12.1.135:/home/user/level02/level02.pcap ."

On l'ouvre dans Wireshark, puis on suit le flux TCP.

On a alors notre mot de passe affiche en clair... avec des points.
Chacun de ces points correspond a une supression de caractere.

Ainsi, on passe du mot de passe "ft_wandr...NDRel.L0L"
au mot de passe: "ft_waNDReL0L"

On utilise alors la commande "su flag02" avec notre mot de passe, puis getflag pour trouver le flag.
Pour acceder au niveau suivant: "su level03" avec notre flag en mot de passe.
