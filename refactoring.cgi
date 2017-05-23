#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import cgi
################ <head> #########################################
print """Content-Type: text/html; charset=UTF-8\n\n
<html>
<head>
<title>Protein Mutation</title>
<script src='Jmol.js' type='text/javascript'>
</script>
<link rel="stylesheet" type="text/css" href="c.css">
</head>"""
########### table作成関数 ########################################
def table_start():
    print"""<table><tr><td>"""

def table_insert():
    print"""</td><td>"""

def table_end():
    print"""</td></tr></table>"""

def ta2():
    print"""</tr><td>"""
###############################################################
def newline():
    print"<br>"

def selectmenu():
    protein_ids = open('rittaisequence.txt','r')
    protein_ids = protein_ids.read()
    protein_id_list = protein_ids.split("\n")
    print"<div class='selection'>"
    print"""<p><span style="font-size:20;">Please select sequence</span>(<span style="font-size:15;">ex:TcCLB.511511.90)</span></p>"""
    print'<form method="post" action="refactoring.cgi">'
    print'<input type="text" list="example"name="text">'
    print'<datalist id="example">'
    for i in protein_id_list:
        print'<option value="%s"></option>'%i
    print'</datalist>'
    print'</select>'
    print'</form>'
    print"</div>"


def horizon():
    print"<hr>"

def color(x,y,z):
    if y<= x <= z:
        print'<span style="background-color:lightgrey">'
def colortozi(x,y,z):
    if y<= x <= z:
        print"</span>"

def henicolorall(count,iro,iro2,heni1,heni2,heni3,heni4,heni5,heni6):
    info =""
    x = 0
    for i in [heni1,heni2,heni3,heni4,heni5,heni6]:
        if i.find(";%s;"%count)>0:
            x += 1
            tmp = i.find(";%s;"%count)
            info += i[tmp-1:tmp+len("%s"%count)+3]
            info += " "
            tmp2=i.find("&")
            tmp3=i.find("$")
            info += i[tmp2:tmp3+1]
    info2 = info.replace(";","")
    info2 = info2.replace("&","")
    if x == 1:
        a = count-iro+1
        print"""<span style="color:red;cursor:n-resize" title="%s" onclick="highlight(%d,%d,%d,%d);henimenu('%s','%s');"> """%(info,a,iro,iro2,x,info2,ttt)
        return count
    if x == 2:
        a = count-iro+1
        print"""<span style="color:darkviolet;cursor:n-resize" title="%s" onclick="highlight(%d,%d,%d,%d);henimenu('%s','%s');">"""%(info,a,iro,iro2,x,info2,ttt)
        return count
    if x >= 3:
        a=count-iro+1
        print"""<span style="color:blue;cursor:n-resize" title="%s" onclick="highlight(%d,%d,%d,%d);henimenu('%s','%s');">"""%(info,a,iro,iro2,x,info2,ttt)
        return count
    
def henicolorendall(count,heni1,heni2,heni3,heni4,heni5,heni6):
    x = 0
    for i in [heni1,heni2,heni3,heni4,heni5,heni6]:
        if i.find(";%s;"%count)>0:
            x += 1
    if x >= 1:    
        print"</span>"


def heniDB(strain,key):
    f = open("queryDB/%squery.txt"%strain)
    x = f.read()
    start = x.find(key)
    henistart = x.find("\n",start)+1
    heniend = x.find("Title",henistart)
    return x[henistart:heniend]
    f.close


###############################################################

print"<body>"
print"<h1><i>Mutation checker for Drug Target protein selection</i></h1>"
horizon()
selectmenu()
newline()

post_id = cgi.FieldStorage()

ttt = post_id.getfirst('text', '')

#print"""<p>T.cruzi CLBrener-NonEsmeraldo-like</p>"""
if ttt:
    print"""<p>ID:%s</p>"""%ttt
#print"""<table border="1" width="400" height="100" background-color="silver"class="menu" ><tr><th>変異 比較株</th></tr>"""
print"""<span id ="targetText"> </span>"""

print"<script  type='text/javascript' >"
print"""function henimenu(info,ttt){ var n = info.split("$").length - 1; var replaced = "<table border ><tr><td>変異</td><td>比較株ID</td></tr><tr>" + info.split("$").slice(0, n).map(function (x) { return "<td>" + x.split(" ").join("</td><td>") + "</td>" } ).join("</tr><tr>") + "</tr></table>"; document.getElementById('targetText').innerHTML = replaced; }"""
print"</script>"

newline()

########################core####################################
table_start()
print'<h3>Amino Acid Sequence</h3>'
table_insert()
print'<h3>Protein 3D Structure(Prediction Model)</h3>'
ta2()
########################配列出力################################
print'<div class="core" style="overflow-y:scroll;overflow-x:hidden;">'
#f = open('proteinid.txt','r')
#new = f.read()
#print new.split("\n")
print"<p>"
print"<b>"
print ttt
print"</b>"
print"</p>"

heni1 = heniDB("CLBEsmeraldo",ttt)
heni2 = heniDB("EsmeORF",ttt)
heni3 = heniDB("Sylvio",ttt)
heni4 = heniDB("Dm28c",ttt)
heni5 = heniDB("JRcl",ttt)
heni6 = heniDB("Tulacl",ttt)



newline()
f = open('db/Tcruzi-s/TriTrypDB-9.0_TcruziCLBrenerNon-Esmeraldo-like_AnnotatedProteins.fasta','r')
text = f.read()
f.close()
#risest = 0

####################### 3d structure sequence###########################
rittaiseq=""
count = 0

if ttt:
    f = open("alifiles/%s.ali"%ttt,'r')
    pdbdata = f.read()
    split = pdbdata.split("\n")
    for i in split:
        count+=1
        if count==3:
            rittaiseq = i.replace("*","")
    #        print rittaiseq
    #rittaiseq = "PPVYPVTVPFLGHIVQFGKNPLEFMQRCKRDLKSGVFTISIGGQRVTIVGDPHEHSRFFSPRNEILSPREVYTIMTPVFGEGVAYAAPYPRMREQLNFLAEELTIAKFQNFVPAIQHEVRKFMAENWKEDEGVINLLEDCGAMIINTACQCLFGEDLRKRLNARHFAQLLSKMESSLIPAAVFMPWLLRLPLPQSARCREARAELQKILGEIIVAREKEEASKDNNTSDLLGGLLKAVYRDGTRMSLHEVCGMIVAAMFAGQHTSTITTSWSMLHLMHPKNKKWLDKLHKEIDEFPAQLNYDNVMDEMPFAERCVRESIRRDPPLLMVMRMVKAEVKVGSYVVPKGDIIACSPLLSHHDEEAFPNPRLWDPERDEKVDGAFIGFGAGVHKCIGQKFALLQVKTILATAFREYDFQLLRDEVPDPDYHTMVVGPTLNQCLVKYTRKKKLPS"
    f.close()

####################################################################

#ttt = "TcCLB.509065.180"

######################3D struction range##################
f = open('kaigyounashi.txt','r')
no_newline_protein = f.read()
riseqst = no_newline_protein.find(rittaiseq)
tttst = no_newline_protein.find(ttt+";")
iro = riseqst-len(ttt)-tttst
#if ttt:    
#    print iro
iro2 = iro + len(rittaiseq)-1
#if ttt:
#    print iro2
###################################################################

start = text.find(ttt+" ")
end = text.find("\n",start)
#print text[end:end+100]
count = 1
if ttt:
    print'<table align="center" width="620">'
    while text[end] != ">":
        print"<tr>"
        print"<td>%d</td>"%count
        for j in range(50):
            if text[end]!=">":
                if text[end]=="\n":
                    end += 1
                    if text[end]!=(">"):
                        print"<td>"
                        color(count,iro,iro2)
                        henicolorall(count,iro,iro2,heni1,heni2,heni3,heni4,heni5,heni6)
                        print"%s"%text[end]
                        henicolorendall(count,heni1,heni2,heni3,heni4,heni5,heni6)
                        colortozi(count,iro,iro2)
                        print"</td>"
                        count+=1
                else:
                    end += 1
                    if text[end]!="\n":
                        print"<td>"
                        color(count,iro,iro2)
                        henicolorall(count,iro,iro2,heni1,heni2,heni3,heni4,heni5,heni6)
                        print"%s"%text[end]
                        henicolorendall(count,heni1,heni2,heni3,heni4,heni5,heni6)
                        colortozi(count,iro,iro2)
                        print"</td>"
                        count+=1
                    else:
                        end += 1
                        if text[end]!=">":
                            print"<td>"
                            color(count,iro,iro2)
                            henicolorall(count,iro,iro2,heni1,heni2,heni3,heni4,heni5,heni6)
                            print"%s"%text[end]
                            henicolorendall(count,heni1,heni2,heni3,heni4,heni5,heni6)
                            colortozi(count,iro,iro2)
                            print"</td>"
                            count+=1
        print"</tr>"
    print"</table>"
    print"</div>"
print"</div>"
################################################################
table_insert()
#####################立体構造出力###############################
print"<script type='text/javascript' >"
#print"jmolApplet(500, 'load db/Tcruzi-s/pdb-structure/models1221/TcCLB.508041.10.B99990001.pdb; cartoons; ');" 
print"jmolSetAppletColor('black');"

if "load protein3dstructures/%s.B99990001.pdb"%ttt:
    print"jmolApplet(500, 'load protein3dstructures/%s.B99990001.pdb; cartoon only; colour whitesmoke;');"%ttt
    for i in range(count):
        x = 0
        for i in [heni1,heni2,heni3,heni4,heni5,heni6]:
            if i.find(";%s;"%i) > 0:
                print"jmolScript('select %d')"%(i-iro+1)
                x += 1
        if x == 1:
            print"jmolScript('colour red')"
        if x == 2:
            print"jmolScript('colour darkviolet')"
        if x == 3:
            print"jmolScript('colour blue')"
else:
    print "prediction model don't exist"

print"var tmp;"
print"var color;"
print"function highlight(t,iro,iro2,x){"
#print'    document.write( " ")'
#print'    document.write( iro2-iro)'
#print'    document.write( " ")'
print"    if(1<=t&&t<=iro2-iro){"
print"        if (tmp!=undefined){"
print"        jmolScript('select '+tmp);}"
print"        if(color!=undefined){"
print"          if (color==1){jmolScript('colour red');}"
print"          if (color==2){jmolScript('colour darkviolet');}"
print"          if (color==3){jmolScript('colour blue');}}"
print"        jmolScript('zoom 0'   );"
print"        jmolScript('cartoon only');"
print"        jmolScript('select '+String(t));"
print"        tmp = String(t);"
print"        color = x;"
print"        jmolScript('spacefill 1.0');"
#print"        jmolScript('set(highlights)');"
print"        jmolScript('colour yellow');"
print"        jmolScript('center selected'   );"
print"        jmolScript('zoomto'   );"
print"    }"
print"}"
print"</script>"
################################################################
table_end()
################################################################
newline()
newline()
print "</body>"
print "</html>"

