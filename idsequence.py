import re

f = open('db/Tcruzi-s/TriTrypDB-9.0_TcruziCLBrenerNon-Esmeraldo-like_AnnotatedProteins.fasta','r')

 
lines2 = f.readlines()
f.close()
for line in lines2:
    print line,
print

