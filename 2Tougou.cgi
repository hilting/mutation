#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import cgi
################ 関数 #########################################
print "Content-Type: text/html; charset=UTF-8\n\n"
print "<html>"
print "<head>"
print "<title>Protein Mutation</title>"
print"<script src='Jmol.js' type='text/javascript'>"
print"</script>"
print'<link rel="stylesheet" type="text/css" href="c.css">'
print"</head>"
########### table作成関数 ########################################
'''def table(x,y):
    print"<table>"
    print"<tr>"
    print"<td>"
    print"x"
    print"</td>"
    print"<td>"
    print"y"
    print"</td>"
    print"</tr>"
    print"</table>"
    '''

def ta_st():
    print"<table>"
    print"<tr>"
    print"<td>"

def ta_in():
    print"</td>"
    print"<td>"

def ta_en():
    print"</td>"
    print"</tr>"
    print"</table>"

def ta2():
    print"</tr>"
    print"<td>"
###############################################################
#def menu():
#    print'<div id="menu">'
#    print'<ul>'
#    print'<li><a href="http://www.cb.cs.titech.ac.jp/~oishi/">TOP</a></li>'
#    print'<li><a href="c.css">ABOUT</a></li>'
#    print'</ul>' 
#    print'</div>'


def neli():
    print"<br>"


def selectmenu():
    f = open('rittaisequence.txt','r')
    new = f.read()
    ID = new.split("\n")
    print"<div class='selection'>"
    print"""<p><span style="font-size:20;">Please select sequence</span>(<span style="font-size:15;">ex:TcCLB.511511.90)</span></p>"""
    print'<form method="post" action="2Tougou.cgi">'
    #print'<select name="example">'
    print'<input type="text" list="example"name="text">'
    print'<datalist id="example">'
    for i in ID:
        #print'<option value="サンプル1">%s</option>'%i
        print'<option value="%s"></option>'%i
    print'</datalist>'
    print'</select>'
    print'</form>'
    print"</div>"


def hr():
    print"<hr>"

def color(x,y,z):
    if y<= x <= z:
        print'<span style="background-color:lightgrey">'
def colortozi(x,y,z):
    if y<= x <= z:
        print"</span>"

#def henicolor(count,heni1):
#    if heni1.find(";%s;"%count) > 0:
#        print'<span style="color:red">'
#        return count
#def henicolorend(count,heni1):
#    if heni1.find(";%s;"%count)>0:
#        print"</span>"    


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


###############################################################

"""
if (info.find("TcCLB"){
    a="T.cruzi CLBrenerEsmeraldolike"
}

if (info.find("SYLVIO"){
    a="T.cruzi Sylvio"
}

if (info.find("TCDM"){
    a="T.cruzi Dm28c"
}

if (info.find("ANOX"){
    a="CLBrenerEsmeraldolike"
}

if (info.find("AODP"){
    a="JRcl"
}

if (info.find("AQHO"){
    a="JRcl"
}
"""

print"<body>"
print"<h1><i>Mutation checker for Drug Target protein selection</i></h1>"
#menu()
hr()
selectmenu()
neli()

f = cgi.FieldStorage()

ttt = f.getfirst('text', '')

#print"""<p>T.cruzi CLBrener-NonEsmeraldo-like</p>"""
if ttt:
    print"""<p>ID:%s</p>"""%ttt
#print"""<table border="1" width="400" height="100" background-color="silver"class="menu" ><tr><th>変異 比較株</th></tr>"""
print"""<span id ="targetText"> </span>"""

print"<script  type='text/javascript' >"
print"""function henimenu(info,ttt){ var n = info.split("$").length - 1; var replaced = "<table border ><tr><td>変異</td><td>比較株ID</td></tr><tr>" + info.split("$").slice(0, n).map(function (x) { return "<td>" + x.split(" ").join("</td><td>") + "</td>" } ).join("</tr><tr>") + "</tr></table>"; document.getElementById('targetText').innerHTML = replaced; }"""
print"</script>"

neli()

########################core####################################
ta_st()
print'<h3>Amino Acid Sequence</h3>'
ta_in()
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



neli()
f = open('db/Tcruzi-s/TriTrypDB-9.0_TcruziCLBrenerNon-Esmeraldo-like_AnnotatedProteins.fasta','r')
text = f.read()
f.close()
#risest = 0

####################### 3d structure sequence###########################
rittaiseq=""
count = 0

if ttt:
    #f = open("alifiles/%s.ali"%ttt,'r')
    #pdbdata = f.read()
    #split = pdbdata.split("\n")
    #for i in split:
    #    count+=1
    #    if count==3:
    #        rittaiseq = i.replace("*","")
    #        print rittaiseq
    rittaiseq = "PPVYPVTVPFLGHIVQFGKNPLEFMQRCKRDLKSGVFTISIGGQRVTIVGDPHEHSRFFSPRNEILSPREVYTIMTPVFGEGVAYAAPYPRMREQLNFLAEELTIAKFQNFVPAIQHEVRKFMAENWKEDEGVINLLEDCGAMIINTACQCLFGEDLRKRLNARHFAQLLSKMESSLIPAAVFMPWLLRLPLPQSARCREARAELQKILGEIIVAREKEEASKDNNTSDLLGGLLKAVYRDGTRMSLHEVCGMIVAAMFAGQHTSTITTSWSMLHLMHPKNKKWLDKLHKEIDEFPAQLNYDNVMDEMPFAERCVRESIRRDPPLLMVMRMVKAEVKVGSYVVPKGDIIACSPLLSHHDEEAFPNPRLWDPERDEKVDGAFIGFGAGVHKCIGQKFALLQVKTILATAFREYDFQLLRDEVPDPDYHTMVVGPTLNQCLVKYTRKKKLPS"
    #f.close()

####################################################################

#ttt = "TcCLB.509065.180"

######################3D struction range##################
f = open('kaigyounashi.txt','r')
kensaku = f.read()
riseqst = kensaku.find(rittaiseq)
tttst = kensaku.find(ttt+";")
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
################################################################
ta_in()
#####################立体構造出力###############################
print"<script type='text/javascript' >"
#print"jmolApplet(500, 'load db/Tcruzi-s/pdb-structure/models1221/TcCLB.508041.10.B99990001.pdb; cartoons; ');" 
print"jmolSetAppletColor('black');"


if "load protein3dstructures/%s.B99990001.pdb"%ttt:
    print"jmolApplet(500, 'load protein3dstructures/%s.B99990001.pdb; cartoon only; colour whitesmoke;');"%ttt

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
#print"        jmolScript('set(highlights)');"
print"        jmolScript('colour yellow');"
print"        jmolScript('center selected'   );"
print"        jmolScript('zoomto'   );"
print"    }"
print"}"




#jmolApplet(300); 
print"</script>"
################################################################
ta_en()
################################################################
################## Mutation place ##################################
"""

if ttt:
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
neli()
mu1=0
mu2=0
mu3=0
mu4=0
if ttt:
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

neli()

if ttt:
    print"%s箇所の変異が見つかりました"%(mu1 - mu2 -mu3)
"""

#################################################################
neli()
neli()
print "</body>"
print "</html>"

