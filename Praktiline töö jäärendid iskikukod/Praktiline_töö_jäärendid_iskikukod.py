while True:
        i=input("Anna sinu isikukood: ")
        if len(i)!=11:
            print("Liiga palju!")
        else:
            print("kirjuta õige!!")

            i_list=list(i)
            print(i_list[0])
            s1=int(i_list[0])
        if s1 not in [1, 2, 3, 4, 5, 6]:
            print("Sümbol ei soobib!!!")
        else:
            print("Esimine sümbool on õige!")
            i_list=list(i)
            a=(i_list[1]+i_list[2])#aastane
            k=int(i_list[3]+i_list[4])#kuud
            p=int(i_list[5]+i_list[6])#päeva
            if ((k)<1 or (k)>13) and ((p)<1 or (p)>31):
                print("Sümipäev ei saanud")
            else:
                if s1==1 or s1==2:
                    y="18"
                elif s1==3 or s1==4:
                    y="19"
                else:
                    y="20"
                pp=str(p)+"."+str(k)+"."+y+str(a)
                print(f"Sünipäev on {pp}")

                Summa=i_list[0]*3 + i_list[1]*7 + i_list[2]*6 + i_list[3]*0 + i_list[4]*5 + i_list[5]*0 + i_list[6]*3 + i_list[7]*0 + i_list[8]*2 + i_list[9]*9
                print(f"Viimane number: {i_list[-1]}")
                s=int(i_list[-1])
                S1=s/11
                S2=S1*11
                print(f"Viimane number2: {S2}")
                continue
       
                
                

                
