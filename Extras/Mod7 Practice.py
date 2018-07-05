#!/usr/bin/env python3
FILENAME = "members.txt"

def _write(members = []):
    with open(FILENAME, "w") as file:
        for m in members:
            file.write(m + "\n")

def _read(members = []):
    count = 0
    with open (FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            members.append(line)
            
            print(str(count+1) + ". " + members[count])
            count += 1

def main():
    members = ["Smith", "John", "Bob"]
    
    while True:
        cmd = str(input(">> "))

        if cmd.lower() == "read":
            _read()
        elif cmd.lower() == "write":
            _write(members)
        else:
            print("\n\"" + cmd + "\" not found.")

if __name__ == "__main__":
    main()
