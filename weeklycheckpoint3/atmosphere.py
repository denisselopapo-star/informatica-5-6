def main():

    layer = input("Descent atmosphere layer: ").strip().lower()


    if layer == "Exosphere":
        print("Your altitude level will be between 700 and 10000 km")
    elif layer == "Thermosphere":
        print("Your altitude level will be between 85 and 700 km")
    elif layer == "Mesosphere":
        print("Your altitude level will be between 50 and 85 km")
    elif layer == "Stratosphere":
        print("Your altitude level will be between 12 and 50 km")
    elif layer == "Troposphere":
        print("Your altitude level will be between 0 and 12 km")
    else:
        print("try again")

        #operations
    altitude = float(input("Enter exact altitude: "))
    time = 0
    if altitude > 700:
        time += (altitudee - 700)/2
        altitude = 700
    if altitude > 85:
        time += (altitude-85)/0.5
        altitude = 85
    if altitude > 50:
        time += (altitude-50)/0.2
        altitude = 50
    if altitude > 12:
        time += (altitude-12)/0.075
        altitude = 12
    time+=altitude/0.02
    print("Total time:", round(time,1))



    #dis1 =9300+615+35+38+12
    #dis2 =615+35+38+12
    #dis3 =35+38+12
    #dis4 =38+12
    #dis5 =12

    #vel1 = 2000+500+200+75+20
    #vel2 = 500+200+75+20
    #vel3 = 200+75+20
    #vel4 = 75+20
    #vel5 = 20

    #dis1 /= vel1
    #dis2 /= vel2
    #dis3 /= vel3
    #dis4 /= vel4
    #dis5 /= vel5



    #if altitude >= 700:
        #print(f"total decent time is {dis1}")
    #elif altitude > 85 :
        #print(f"total decent time is {dis2}")
    #elif altitude > 50 :
        #print(f"total decent time is {dis3}")
    #elif altitude > 12 :
        #print(f"total decent time is {dis4}")
    #elif altitude > 85 :
        #print(f"total decent time is {dis5}")
    #else:
        #print()


if __name__=="__main__":
    main()

