#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import cgi
##  header ###########################################################
print"""Content-Type: text/html; charset=UTF-8\n\n
<html>
<head>
<title>Mutation checker for Drug Target protein selection</title>
<script src='Jmol.js' type='text/javascript'>
</script>
<link rel="stylesheet" type="text/css" href="c.css">
</head>"""
## function ##########################################################
## table_create
def table_begin():
    print"<table><tr><td>"

def table_inner():
    print"</td><td>"

def table_end():
    print"</td></tr></table>"

def table_inner2():
    print"</tr><td>"

def new_line():
    print"<br>"

## protein_id_selection
def select_id():
    f = open('protein_id.txt','r')
    protein_id = f.read().split("\n")
    f.close
    print"""<div class='selection'>
    <p><span style="font-size:20;">Please select sequence</span>(<span style="font-size:15;">ex:TcCLB.511511.90)</span></p>
    <form method="post" action="2Tougou.cgi">
    <input type="text" list="example"name="text">
    <datalist id="example">"""
    for i in protein_id:
        print'<option value="%s"></option>'%i
    print'</datalist>'
    print'</select>'
    print'</form>'
    print"</div>"

def horizon():
    print"<hr>"

## prediction model grey color
def color(x,y,z):
    if y<= x <= z:
        print'<span style="background-color:lightgrey">'
def colortozi(x,y,z):
    if y<= x <= z:
        print"</span>"

def henicolorall(count,iro,iro2,heni1,heni2,heni3,heni4,heni5,heni6):
    info =""
    x = 0
    if heni1.find(";%s;"%count)>0:
        x += 1
        tmp = heni1.find(";%s;"%count)
        info += heni1[tmp-1:tmp+len("%s"%count)+3]
        info += " "
        tmp2=heni1.find("&")
        tmp3=heni1.find("$")
        info += heni1[tmp2:tmp3+1]
    if heni2.find(";%s;"%count)>0:
        x += 1
        tmp = heni2.find(";%s;"%count)
        info += heni2[tmp-1:tmp+len("%s"%count)+3]
        info += " "
        tmp2=heni2.find("&")
        tmp3=heni2.find("$")
        info += heni2[tmp2:tmp3+1]
    if heni3.find(";%s;"%count)>0:
        x += 1
        tmp = heni3.find(";%s;"%count)
        info += heni3[tmp-1:tmp+len("%s"%count)+3]
        info += " "
        tmp2=heni3.find("&")
        tmp3=heni3.find("$")
        info += heni3[tmp2:tmp3+1]
    if heni4.find(";%s;"%count)>0:
        x += 1
        tmp = heni4.find(";%s;"%count)
        info += heni4[tmp-1:tmp+len("%s"%count)+3]
        info += " "
        tmp2=heni4.find("&")
        tmp3=heni4.find("$")
        info += heni4[tmp2:tmp3+1]
    if heni5.find(";%s;"%count)>0:
        x += 1
        tmp = heni5.find(";%s;"%count)
        info += heni5[tmp-1:tmp+len("%s"%count)+3]
        info += " "
        tmp2=heni5.find("&")
        tmp3=heni5.find("$")
        info += heni5[tmp2:tmp3+1]
    if heni6.find(";%s;"%count)>0:
        x += 1
        tmp = heni6.find(";%s;"%count)
        info += heni6[tmp-1:tmp+len("%s"%count)+3]
        info += " "
        tmp2=heni6.find("&")
        tmp3=heni6.find("$")
        info += heni6[tmp2:tmp3+1]
    info2 = info.replace(";","")
    info2 = info2.replace("&","")
    if x == 1:
        a = count-iro+1
        print"""<span style="color:red;cursor:n-resize" title="%s" onclick="highlight(%d,%d,%d,%d);henimenu('%s','%s');"> """%(info,a,iro,iro2,x,info2,formed_id)
        return count
    if x == 2:
        a = count-iro+1
        print"""<span style="color:darkviolet;cursor:n-resize" title="%s" onclick="highlight(%d,%d,%d,%d);henimenu('%s','%s');">"""%(info,a,iro,iro2,x,info2,formed_id)
        return count
    if x >= 3:
        a=count-iro+1
        print"""<span style="color:blue;cursor:n-resize" title="%s" onclick="highlight(%d,%d,%d,%d);henimenu('%s','%s');">"""%(info,a,iro,iro2,x,info2,formed_id)
        return count
    
def henicolorendall(count,heni1,heni2,heni3,heni4,heni5,heni6):
    x = 0
    if heni1.find(";%s;"%count)>0:
        x += 1
    if heni2.find(";%s;"%count)>0:
        x += 1
    if heni3.find(";%s;"%count)>0:
        x += 1
    if heni4.find(";%s;"%count)>0:
        x += 1
    if heni5.find(";%s;"%count)>0:
        x += 1
    if heni6.find(";%s;"%count)>0:
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



## main start #########################################################
print"<body>"
print"<h1><i>Mutation checker for Drug Target protein selection</i></h1>"
horizon()
select_id()
new_line()

## compare info
formed_item = cgi.FieldStorage()
formed_id = formed_item.getfirst('text', '')
if formed_id:
    print"""<p>ID:%s</p>"""%formed_id
print"""<span id="targetText"> </span><script type='text/javascript'>"""
print"""function henimenu(info,formed_id){ var n = info.split("$").length - 1; var replaced = "<table border ><tr><td>変異</td><td>比較株ID</td></tr><tr>" + info.split("$").slice(0, n).map(function (x) { return "<td>" + x.split(" ").join("</td><td>") + "</td>" } ).join("</tr><tr>") + "</tr></table>"; document.getElementById('targetText').innerHTML = replaced; }"""
print"</script>"
new_line()



## amino acid sequence & protein structure ################################
table_begin()
print'<h3>Amino Acid Sequence</h3>'
table_inner()
print'<h3>Protein 3D Structure(Prediction Model)</h3>'
table_inner2()



## Amino acid sequence ######################################################
print'<div class="core" style="overflow-y:scroll;overflow-x:hidden;">'
#f = open('proteinid.txt','r')
#new = f.read()
#print new.split("\n")
print"<p><b>"
print formed_id
print"</b></p>"
heni1 = heniDB("CLBEsmeraldo",formed_id)
heni2 = heniDB("EsmeORF",formed_id)
heni3 = heniDB("Sylvio",formed_id)
heni4 = heniDB("Dm28c",formed_id)
heni5 = heniDB("JRcl",formed_id)
heni6 = heniDB("Tulacl",formed_id)
new_line()



## 3d structure sequence
## 変数宣言
mode_seq = ""
if formed_id:
    ## alifilesはmodellerで作成した予測モデルのアミノ酸配列
    f = open("alifiles/%s.ali"%formed_id,'r')
    modeller_sequence = f.read()
    f.close()
    modeller_sequence_list = modeller_sequence.split("\n")
    mode_seq = modeller_sequence_list[2].replace("*","")
    ## デバッグ用
    #print mode_seq
    #mode_seq = "PPVYPVTVPFLGHIVQFGKNPLEFMQRCKRDLKSGVFTISIGGQRVTIVGDPHEHSRFFSPRNEILSPREVYTIMTPVFGEGVAYAAPYPRMREQLNFLAEELTIAKFQNFVPAIQHEVRKFMAENWKEDEGVINLLEDCGAMIINTACQCLFGEDLRKRLNARHFAQLLSKMESSLIPAAVFMPWLLRLPLPQSARCREARAELQKILGEIIVAREKEEASKDNNTSDLLGGLLKAVYRDGTRMSLHEVCGMIVAAMFAGQHTSTITTSWSMLHLMHPKNKKWLDKLHKEIDEFPAQLNYDNVMDEMPFAERCVRESIRRDPPLLMVMRMVKAEVKVGSYVVPKGDIIACSPLLSHHDEEAFPNPRLWDPERDEKVDGAFIGFGAGVHKCIGQKFALLQVKTILATAFREYDFQLLRDEVPDPDYHTMVVGPTLNQCLVKYTRKKKLPS"
#formed_id = "TcCLB.509065.180"




## 3D structure range
f = open('kaigyounashi.txt','r')
kensaku = f.read()
riseqst = kensaku.find(mode_seq)
formed_idst = kensaku.find(formed_id+";")
iro = riseqst-len(formed_id)-formed_idst
iro2 = iro + len(mode_seq)-1


f = open('db/Tcruzi-s/TriTrypDB-9.0_TcruziCLBrenerNon-Esmeraldo-like_AnnotatedProteins.fasta','r')
## textはCLBnonEsmのfastaファイル
text = f.read()
f.close()
start = text.find(formed_id+" ")
end = text.find("\n",start)
count = 1
if formed_id:
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
        #count -= 1
        print"</tr>"
        #count += 1
    print"</table>"
    print"</div>"

#start = 0
#for i in range(1,20):
#    id_start = txt2.find('>',start)
#    print txt2[id_start:id_start+17]
#    start += (id_start +2 -txt2.find('>',start-2))
print"</div>"
table_inner()
## 立体構造出力 ###########################################
print"<script type='text/javascript' >"
#print"jmolApplet(500, 'load db/Tcruzi-s/pdb-structure/models1221/TcCLB.508041.10.B99990001.pdb; cartoons; ');" 
print"jmolSetAppletColor('black');"
if "load protein3dstructures/%s.B99990001.pdb"%formed_id:
    print"jmolApplet(500, 'load protein3dstructures/%s.B99990001.pdb; cartoon only; colour whitesmoke;');"%formed_id
    for i in range(count):
        x = 0
        if heni1.find(";%s;"%i) > 0:
            print"jmolScript('select %d')"%(i-iro+1)
            x += 1
        if heni2.find(";%s;"%i) > 0:
            print"jmolScript('select %d')"%(i-iro+1)
            x += 1
        if heni3.find(";%s;"%i) > 0:
            print"jmolScript('select %d')"%(i-iro+1)
            x += 1
        if heni4.find(";%s;"%i) > 0:
            print"jmolScript('select %d')"%(i-iro+1)
            x += 1
        if heni5.find(";%s;"%i) > 0:
            print"jmolScript('select %d')"%(i-iro+1)
            x += 1
        if heni6.find(";%s;"%i) > 0:
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
print"        jmolScript('colour yellow');"
print"        jmolScript('center selected'   );"
print"        jmolScript('zoomto'   );"
print"    }"
print"}"

#jmolApplet(300); 
print"</script>"
table_end()
################## Mutation place ##################################
"""
if formed_id:
    print"mutation place on the 3D structure="        
for i in range(count):
    if heni1.find(";%s;"%i) > 0:
        if i-iro+1 > 0:
            print i-iro+1
    if heni2.find(";%s;"%i) > 0:
        if i-iro+1 > 0:
            print i-iro+1
    if heni3.find(";%s;"%i) > 0:
        if i-iro+1 > 0:
            print i-iro+1
    if heni4.find(";%s;"%i) > 0:
        if i-iro+1 > 0:
            print i-iro+1
    if heni5.find(";%s;"%i) > 0:
        if i-iro+1 > 0:
            print i-iro+1
    if heni6.find(";%s;"%i) > 0:
        if i-iro+1 > 0:
            print i-iro+1
new_line()
mu1=0
mu2=0
mu3=0
mu4=0
if formed_id:
    print"mutation place="
for i in range(count):
    mu0=0
    if heni1.find(";%s;"%i) > 0:
        print i
        mu0 += 1
    if heni2.find(";%s;"%i) > 0:
        print i
        mu0 += 1
    if heni3.find(";%s;"%i) > 0:
        print i
        mu0 += 1
    if heni4.find(";%s;"%i) > 0:
        print i
        mu0 += 1
    if heni5.find(";%s;"%i) > 0:
        print i
        mu0 += 1
    if heni6.find(";%s;"%i) > 0:
        print i
        mu0 += 1
    mu1 += mu0
    if mu0 == 2:
        print "<%s>"%i
        mu2 += 1
    if mu0 == 3:
        print"<;%s;>"%i
        mu3 += 2
    if mu0 ==4:
        print"<;%s;>"%i
        mu4+=3

new_line()

if formed_id:
    print"%s箇所の変異が見つかりました"%(mu1 - mu2 -mu3)
"""
new_line()
new_line()
print "</body>"
print "</html>"
