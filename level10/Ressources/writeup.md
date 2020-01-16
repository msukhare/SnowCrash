token to flag10 = woupa2yuojeeaaed06riuj63c

Check flag.Here is your token : feulo4b72j7edeahuete3no7c

Nous avons commence par regarder le binaire fourni avec strings:

strings level10

puis nous avons trouve la fonction access, a la lecture du man nous nous sommes
rendu compte qu'elle avait une fail de securite. Nous avons trouve "race condition"

lien sur le race condition:

https://samsclass.info/127/proj/E10.htm
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.210.1202&rep=rep1&type=pdf
https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use

Nous avons donc exploite cette fail.
Nous avons d'abord ouvert une socket grace a open_socket.sh
puis tricks_access.sh qui permet d'intervertir un lien symbolique entre deux fichier
un qui a des droits de lecture et le token qui ne les a pas, en boucle.
Puis nous avons excute exec_command.sh qui permet de lancer le binaire en boucle
afin que la fail reussi.

Resume de la fail:

Lors de l'execution du binaire le parametre passe sera le lien symbolique qui
pointera soit vers le fichier token, soit vers le fichier que nous avons cree au prealable
avec les droits necessaire a sa lecture.
A un moment donne le binaire utilisera la fonction access sur le fichier avec les
bonnes permissions puis le script charge d'intervertir le lien symbolique
changera de fichier et le fichier qui sera lu ne sera plus notre fichier
mais le fichier "token".
