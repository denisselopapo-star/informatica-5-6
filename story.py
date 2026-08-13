def main():
    # planet = input("Planet:")

    # # Separation
    # print("Hello", planet)
    # # Concatenation
    # print("Hello" + planet)
    # # Formatted Strings
    # print(f"Hello {planet}")
    # # Ending
    # print("Hello", end=" ")
    # print(planet)

    name = input("What is your name?")
    color = input("Tell me a color:")
    goal = input("Tell me a goal:")
    adjective = input("Give me and adjetive:")

    print(f"Hello, {name}!", end="\n\n")

    print("this is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.")

if __name__ =="__main__":
    main()
