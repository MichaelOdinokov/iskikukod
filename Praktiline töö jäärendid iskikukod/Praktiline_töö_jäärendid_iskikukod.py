from Omamodul import *


arvud=[]
isikukood=[]
while True:
    print(isikukood)
    isikukood=naised_mehed(isikukood)#
    print(isikukood)
    arvud=list(map(int, arvud))
    arvud.sort
    print(arvud)

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
            if sp=="Viga":
                arvud.append(i)
            else:
                print(f"Sünipäev on {i}")

                #
                sugu=Sugu(i_list)
                 
                Summa=i_list[0]*3 + i_list[1]*7 + i_list[2]*6 + i_list[3]*0 + i_list[4]*5 + i_list[5]*0 + i_list[6]*3 + i_list[7]*0 + i_list[8]*2 + i_list[9]*9
                s=int(i_list[-1])
                S1=s%11
                S2=S1*11
                print(f"Viimane number: {S2}")
                kontrolnr=S2
                isikukood.append(i)
                haig=a()


                print(haig)
                print(f"See in "+sugu+", sünipäev "+pp+". Ta on sündinud "+haig)
                                    
                print()
                arvud=list(map(int,arvud)) #pere obrazuet
                arvud.sort()
                print(arvud)
                ven=int(input("Закончить цикл?\n1)Jah\n2)Ei\n"))
        if ven==1:
            break
print(n)
print(m)

       
                
                

                

                

                

       
                
                

                
