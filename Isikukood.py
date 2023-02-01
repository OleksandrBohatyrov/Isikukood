from omamoodul import *
#isikukood=input("Sisesta isikukood: ")
#isikukood_list=list(isikukood)
#print(isikukood_list)

ikood=""
while True:
    ikood=input("Sesesta isikukood: ")
    if pikkus(ikood)==False:
        print("Liig pikk või lühike isikukood")
    else:
        s=sugu_check(ikood)
        if s=="viga":
            print("Esimene täht ei ole õige")
        else:
            if sunnipaev(ikood)=="viga":
                print("2-7 tähed on valesti sisestatud")
            else:
                print(sunnipaev(ikood))
                if sunnikoht(ikood)=="viga":
                    print(" asd")
                else:
                    print(lause(ikood))