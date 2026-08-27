def main():

    layer = input("Descent atmosphere layer: ").strip().title()

    Exo = 700, 10000
    The = 85, 700
    Mes = 50, 85
    Str = 12, 50
    Tro = 0, 12

    if layer == Exosphere:
        print(f"Your altitude level will be between {Exo} km")
    elif layer == Thermosphere:
        print(f"Your altitude level will be between {The} km")
    elif layer == Mesosphere:
        print(f"Your altitude level will be between {Mes} km")
    elif layer == Stratosphere:
        print(f"Your altitude level will be between {Str} km")
    elif layer == Troposphere:
        print(f"Your altitude level will be between {Tro} km")
    else:
        print()
        #operations
    altitude = int(input(f"Enter exact altitude: "))
    dis1 =9300+615+35+38+12
    dis2 =615+35+38+12
    dis3 =35+38+12
    dis4 =38+12
    dis5 =12

    vel1 = 2000+500+200+75+20
    vel2 = 500+200+75+20
    vel3 = 200+75+20
    vel4 = 75+20
    vel5 = 20

    dis1 /= vel1
    dis2 /= vel2
    dis3 /= vel3
    dis4 /= vel4
    dis5 /= vel5



    if altitude >= 700:
        print(f"total decent time is {dis1}")
    elif altitude > 85 :
        print(f"total decent time is {dis2}")
    elif altitude > 50 :
        print(f"total decent time is {dis3}")
    elif altitude > 12 :
        print(f"total decent time is {dis4}")
    elif altitude > 85 :
        print(f"total decent time is {dis5}")
    else:
        print()


if __name__=="__main__":
    main()

