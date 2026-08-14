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

    name = input("What is your name?").strip().title()
    color = input("Tell me a color:").strip().lower()
    goal = input("Tell me a goal:").strip().lower()
    adjective = input("Give me and adjetive:").strip().lower()

    print(f"Hello, {name}!", end="\n\n")

    print("this is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.")

    print(f"Hello, {name}!", end="\n\n")

    print("this is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.".upper())


if __name__ =="__main__":
    main()
