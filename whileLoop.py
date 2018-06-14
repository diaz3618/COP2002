def whileLoop(question, choice):
    print()
    while choice.lower() != "n" or choice.lower() != "y":
        choice = input(question)
        if choice.lower() == "n":
            print("\nBye!")
            break

        elif choice.lower() == "y":
            break
        print("please enter y or n")
