
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus

Pour trouver ce flag, nous avons utilise le binaire strings sur le binaire du
level03. Nous avons pu observer que le binaire utilise la commande echo. Par
consequent nous avons cree un lien symbolique avec ln -s sur /bin/getflag et l'avons
mis dans /tmp sous le nom de echo "/tmp/echo". Ensuite nous avons ajoute /tmp dans la variable
d'environemment PATH pour qu'il execute notre lien symbolique qui est getflag a
la place de echo. Cela nous a permit d'obtenir le flag car le binaire exploite
avec les permission sudo.

ln -s /tmp/echo /bin/getflag
export PATH=/tmp:
./level03
