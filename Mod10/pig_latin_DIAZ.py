#!/usr/bin/env python3
VOWELS = ("aeiou")

def _word(word):
    first_letter = word[0]
    if first_letter in VOWELS:
        return word + "way"
    elif first_letter == "y":
        return word[1:] + first_letter + "ay"
    else:
        return word[1:] + first_letter + "ay"  
                                            
def _sentence(sentence):
    _list = sentence.split(' ')
    new_sentence = ""

    for word in _list:
        new_sentence = new_sentence + _word(word)
        new_sentence = new_sentence + " "
    return new_sentence

def _strip(text):
    symbols = ("!@#$%^&*()><{}:?|\;/.,~`")
    
    for i in range(0, len(text)):
            for j in range(0, len(symbols)):
                text = text.strip(symbols[j])
    return text

def IO():
    line = "{:12}"
    line2 = "{:11} {:11}"
    again = "y"

    while again.lower() == "y":
        text = str(input(line.format("Enter text:")))
        text = _strip(text)
        
        print(line2.format("English:", text.lower()))   
        print(line2.format("Pig Latin:", _sentence(text.lower())) + "\n")

        while again.lower() != "n" or again.lower() != "y":
            again = str(input("Continue? (y/n): "))

            if again.lower() == "y":
                print()
                break
            elif again.lower() == "n":
                print("\nBye!")
                break

def main():
    print("Pig Latin Translator\n\n")
    IO()

if __name__ == "__main__":
    main()
