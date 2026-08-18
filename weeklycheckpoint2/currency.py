def main():

    c = float(input("What do you have left in pesos? "))
    p = float(input("What do you have left in soles? "))
    b = float(input("What do you have left in reais? "))
    u = (c * 0.00032)+(p * 0.30)+ (b * 0.19)
    m = (c*0.0054)+(p* 5.07)+(b * 3.17)


if __name__=="__main__":
    main()
