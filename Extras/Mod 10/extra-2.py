import csv
FILENAME = "emails.csv"

def template():
    emails = _read()
    line = "{:9}"

    ## List guide
    print("List guide" + \
          "\nemails[0]: " + str(emails[0]) + \
          "\nemails[0][0]: " + emails[0][0] + \
          "\nemails[0][1]: " + emails[0][1] + \
          "\nemails[0][2]: " + emails[0][2] + "\n")
    
    _to = str(input(line.format("To:")))
    _from = str(input(line.format("From:")))
    _subject = str(input(line.format("Subject:")))

def main():
    template()


## Read data from "emails.csv"
def _read():
    emails = []
    with open(FILENAME, newline = "") as f:
        reader = csv.reader(f)

        for i in reader:
            emails.append(i)
    return emails

## Write data into "emails.csv"
def _write(emails):
    with open(FILENAME, "w", newline = "") as f:
        write = csv.writer(f)
        write.writerows(emails)

if __name__ == "__main__":
    main()
