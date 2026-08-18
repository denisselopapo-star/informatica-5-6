def main():
    l = 5
    w = int(input("Width: "))
    print("o" * w)
    print("o" * w)
    print("o" * w)
    print("o" * w)
    print("o" * w)

    p = (2 * 1) + (2 * w)
    print("Perimeter:",p)
    a = (l * w)
    print("Area:",a)
    d = (l**2+ w**2)
    print("diagonal:",d)

if __name__=="__main__":
    main()
