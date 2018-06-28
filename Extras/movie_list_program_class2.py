#!/usr/bin/env python3

# movie_list program with 2D list

def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("delete - Delete a movie")
    print("exit - Exit program")
    print()

def list(movie_list):
    i = 1
    for row in movie_list:
        print(str(i) + ". " + row[0] + " " + "( "+ str(row[1]) + " ) " + " @   " + str(row[2]))  ## Added (  + "( "+ str(row[1]) + " ) " + " @   " + str(row[2])  )
        i += 1
    print()

def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    price = float(input("Price: ")) ## Added
    movie = []
    movie.append(name)
    movie.append(year)
    movie.append(price) ## Added
    movie_list.append(movie)
    print(movie[0] + " was added to the list.\n")
    

def delete(movie_list):
    movie_number = int(input("Number: "))
    if movie_number < 1 or movie_number > len(movie_list):
        print("Invalid movie number. \n")
    else:
        movie = movie_list.pop(movie_number-1)
        print(movie, " was deleted.\n")
    

def main():
    movie_list = [["Monty Python and the Holy Grail", 1975, 9.95], ["On the Waterfront", 1954, 5.59], ["Cat on a Hot Tin Roof", 1958, 7.95]]
    display_menu()
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list(movie_list)
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "delete":
            delete(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Invalid command. Please try again.")
    print("Bye!")

if __name__ == "__main__":
    main()
        
    
    
        
    
