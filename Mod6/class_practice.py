def menu():
    print("""COMMAND MENU
list - List all movies
add - Add a movie
delete - Delete a movie
exit - Exit program\n""")

def movies():
    movies = [['Terminator', 1984], ['Terminator 2', 1991]]
    return movies

def main():
    test = movies()
    
    i = 0
    for i in test(0,len(test)):
        i += 1
        print(test[i][i] + " " + str(test[i][i+1]))
    print(test[0][0] + " " + str(test[0][1]))
    menu()

if __name__ == "__main__":
    main()
