from omamoodul import *
#isikukood=input("Sisesta isikukood: ")
#isikukood_list=list(isikukood)
#print(isikukood_list)

ikood=""



arvud=[100,1001,211,222]
ikoodid=[]

while True:
    ikood=input("Sesesta isikukood: ")
    if pikkus(ikood)==False:
        print("Liig pikk või lühike isikukood")
        arvud.append(ikood)
    else:
        s=sugu_check(ikood)
        if s=="viga":
            print("Esimene täht ei ole õige")
            arvud.append(ikood)
        else:
            if sunnipaev(ikood)=="viga":
                print("2-7 tähed on valesti sisestatud")
            else:
                print(sunnipaev(ikood))
                if sunnikoht(ikood)==int(ikood[-1]):

                    print("OK")
                    ikood.append(ikood)
                else:
                    print(lause(ikood))
                    print(kontrollnr(ikood))
    print()
    ikoodid=naised_mehed(ikoodid)
    print(ikoodid)
    arvud_sorted(arvud)
    print(arvud)
