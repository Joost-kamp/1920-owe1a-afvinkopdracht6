#Exercise 2 File Head Display

def read_file(name_file):
    """Leest 5 regels van het bestand in

    Input:
    name_file - str - file dat ingelezen moet worden    
    """

    try:
        with open(name_file, "r") as file_open:
            for i in range(0,5):
                regel = file_open.readline()
                print(regel)
    except IOError:
        print("File can't be found")
    except:
        print("Can't the problem")

    
if __name__ == "__main__":
    name_file = input("What is the name of the file: ")
    read_file(name_file)



#Exercise 5 Sum of Numbers

def sum_file(txt_file):
    """Lees het bestand in en geeft de som van de getallen

    Input:
    txt_file - str - het bestand
    """
    try:
        with open(txt_file, "r") as txt_open:
            total = 0
            for line in txt_open:
                num = int(line)
                total += num
            print(total)
    except IOError:
        print("File can't be found")
    except:
        print("Can't find the problem")
                

if __name__ == "__main__":
    txt_file = "numbers.txt"
    sum_file(txt_file)



#Exercise 7 Word List File Writer

def write_file(name_file):
    """Asks the user to enter how many and what words they want to write to the file
    and writes the words to the file

    Input:
    name_file - str - the name of the file
    """

    try: 
        num_words = int(input("How many words would you like to write?: "))
    
        with open(name_file, "w") as write_file:
            for count in range(1, num_words + 1):
                words = input("Enter word #" + str(count) + ": ")
            
                write_file.write(str(words) + "\n")
    except IOError:
        print("File can't be found")
    except ValueError:
        print("Conversion integer failed")
    except:
        print("Can't find the problem")
    


if __name__ == "__main__":
    name_file = "words.txt"
    write_file(name_file)


