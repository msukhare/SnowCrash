your token is 2A31L79asukciNyi8uppkEuSx

Pour resoudre ce challenge nous avons utilise gdb.
Le binaire fourni nous demandait un uid different du notre.
Par consequent nous avons lance gdb puis disas main ensuite nous avons trouve

" 0x0804859a <+14>: cmp    $0x1092,%eax", soit la valeur de retour de getuid,
nous lui avons set un breakpoint "b * 0x0804859a "

Puis nous avons fait la commande suivante "r", pour lancer le programme, 
"set $eax=4242" 4242 pour regler le uid attendu par $eax a 4242, puis "c" pour continuer son execution.

La commande getflag s'effectue alors.
