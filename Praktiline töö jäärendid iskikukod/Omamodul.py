def Sugu(i_list:list)->str:
    """Esimese tahe järgi määrme sugu
    :param list ik_list:Järjend isikukoodi numbridest
    :rtype: str
    """

    if int(i_list[0])%2==0:
        sugu="naine"
    else:
        sugu="mees"
    return sugu


def Sunnikoht(a:int)->str:
    """määrme Sunnikoht #......
    :param int a: Järjend sunnikoht
    :rtype: str
    """
    if 1<=a<=10:
                    haig="kuresaare Higla"
    elif 11<=a<=19:
                    haig="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21<=a<=220:
                    haig="ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif 221<=a<=270:
                    haig="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271<=a<=370:
                    haig="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371<=a<=420:
                    haig="Narva Haigla"
    elif 471<=a<=490:
                    haig="Pärnu Haigla"
    elif 491<=a<=520:
                    haig="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif 521<=a<=570:
                    haig="Järvamaa Haigla (Paide)"
    elif 571<=a<=600:
                    haig="Valga Haigla"
    elif 601<=a<=650:
                    haig="Viljandi Haigla"
    elif 651<=a<=700:
                    haig="Lõuna-Eesti Haigla (Võru), Põlva Haigla "
    return haig

def Sunnipaev(ik_list:list)->str:
     """määrme spaev
     :parem str ik: Järjend spaev
     :rtype: str
     """
     s1=int(ik_list[0])
     y=ik_list[1]+ik_list[2] #aasta
     m=ik_list[3]+ik_list[4] #kuu
     d=ik_list[5]+ik_list[6] #päev
   
     if int(m)<1 or int(m)>13 and int(d)<1 or int(d)>31:
         spaev="Viga"
     else:
         if s1==1 or s1==2:
             yy="18"
         elif s1==3 or s1==4:
             yy="19"
         else:
             yy="20"
         spaev=d+"."+m+"."+yy+y
         return spaev

def naised_mehed(ikoodid:list):
    """E
    :rtype: list
    """
    naised=[]
    mehed=[]
    for kood in ikoodid:
        ik_list=list(kood)
        sugu=Sugu(ik_list)
        if sugu=="naine":
            naised.append(kood)
        else:
            mehed.append(kood)
    ikoodid.clear()
    ikoodid.extend(naised)
    ikoodid.extend(mehed)
    return ikoodid


