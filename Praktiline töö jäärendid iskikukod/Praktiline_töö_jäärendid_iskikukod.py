arvud=[]
isikukood=[]
m=[]#mees
n=[]#naine

while True:
        i=input("Anna sinu isikukood: ")
        if len(i)!=11:
            print("Liiga palju!")
            arvud.append(i)
        else:
            print("kirjuta õige!!")

            i_list=list(i)
            print(i_list[0])
            s1=int(i_list[0])
        if s1 not in [1, 2, 3, 4, 5, 6]:
            print("Sümbol ei soobib!!!")
            arvud.append(i)
        else:
            print("Esimine sümbool on õige!")
            i_list=list(i)
            a=(i_list[1]+i_list[2])#aastane
            k=int(i_list[3]+i_list[4])#kuud
            p=int(i_list[5]+i_list[6])#päeva
            if ((k)<1 or (k)>13) and ((p)<1 or (p)>31):
                print("Sümipäev ei saanud")
                arvud.append(i)
            else:
                if s1==1 or s1==2:
                    y="18"
                elif s1==3 or s1==4:
                    y="19"
                else:
                    y="20"
                pp=str(p)+"."+str(k)+"."+y+str(a)
                print(f"Sünipäev on {pp}")

                if int(i_list[0])%2==0:
                    sugu="Naine"
                else:
                    sugu="Mees"

                Summa=i_list[0]*3 + i_list[1]*7 + i_list[2]*6 + i_list[3]*0 + i_list[4]*5 + i_list[5]*0 + i_list[6]*3 + i_list[7]*0 + i_list[8]*2 + i_list[9]*9
                s=int(i_list[-1])
                S1=s%11
                S2=S1*11
                print(f"Viimane number: {S2}")
                kontrolnr=S2
                isikukood.append(i)
                h=int(i_list[8]+i_list[9]+i_list[10])
                if 1<=h<=10:
                    haig="Kuresaare Haigla"
                elif 11<=h<=19:
                    haig="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
                elif 221<=h<=220:
                    haig="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
                elif 221<=h<=270:
                    haig="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
                elif 271<=h<=370:
                    haig="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
                elif 371<=h<=420:
                    haig="Narva Haigla"
                elif 421<=h<=470:
                    haig="Pärnu Haigla"
                elif 471<=h<=490:
                    haig="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
                elif 491<=h<=520:
                    haig="Järvamaa Haigla (Paide)"
                elif 521<=h<=570:
                    haig="Rakvere, Tapa haigla"
                elif 571<=h<=600:
                    haig="Valga Haigla"
                elif 601<=h<=650:
                    haig="Viljandi Haigla"
                elif 651<=h<=700:
                    haig="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
                    print(haig)
                print(f"See in {sugu}, sünipäev {pp}. Ta on sündinud haigla {haig}")
                print(isikukood)
                isikukood=(m+n)
                
                arvud=list(map(int,arvud)) #pere obrazuet
                arvud.sort()
                print(arvud)

                

       
                
                

                
