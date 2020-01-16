Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub

Nous avons regarde le binaire fourni et nous avons apercu que ce dernier utilise
le script php fourni. Le script php utilise des regex avec /e, /e est vulnerable
et deprecie car celui ci execute les binaire qui lui sont passe.

Nous avons donc execute le binaire level06 avec comme argument 
"[x ${`getflag`}]" afin que la regex fasse les changement et que /e execute
getflag

lien utilise: http://www.madirish.net/402
