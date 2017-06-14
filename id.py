import re
import sys
sys.stdout = open("proteinid.txt","w")

f = open('db/Tcruzi-s/TriTrypDB-9.0_TcruziCLBrenerNon-Esmeraldo-like_AnnotatedProteins.fasta','r')
txt = f.read()

x = re.findall(r'TcCLB............',txt)
for i in x:
    a= i.replace(" |","")
    print a.replace(" ","")

sys.stdout.close()
sys.stdout =sys.__stdout__


