Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ

Etant donne qu'il n'y avait rien dans le dossier du level14 et qu'a l'exercice
precedent on a utilise gdb nous nous sommes dit qu'ici ca allait etre le meme chose
sauf qu'il faudrait le faire pour /bin/getflag.
Nous avons donc regarde la sortie de strings /bin/getflag, nous y avons vu la fonction getuid, mais
aussi la fonction ptrace qui bloque l'utilisation de gdb.

gdb /bin/geflag
disas main
b * 0x0804898e (valeur de retour de ptrace)
b * 0x08048b02 (valeur de retour de getuid)
r
set $eax=0 (pour que le retour de ptrace soit egal a 0 et que le programme ne sort pas ==> ptrace ne bloque pas gdb)
c
set $eax=3014 (pour avoir les droits de flag14 pour executer le programme on obtien ce nombre grace a la comande id -u flag14)
c
