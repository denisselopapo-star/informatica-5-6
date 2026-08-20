def main():
    transitors = 17800000000
    years = int(input("years in the future: "))

    transitors *= 2**(years/2)
    print(f"In {years} this would be the new number of transitors: {transitors}")

if __name__=="__main__":
    main()
