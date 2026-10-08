def main():
    print("Welcome to Binary to Decimal Converter!")
    print("The purpose of this program is to convert binary numbers to a decimal number")
    user_num = int(input("Enter a binary number: "))
    dec = 0

def binary_to_decimal(numbers):
    list = [128,64,32,16,8,4,2,1]
    for i in user_num:
        list.append(user_num [i])
        list.sort(reverse = True)
        for i in range(lens(list)):
            dec = dec+2**(i+1)
        if i == 1:
            print(f"Decimal number: {dec}" )
        else:
            print()




if __name__=="__main__":
    main()
