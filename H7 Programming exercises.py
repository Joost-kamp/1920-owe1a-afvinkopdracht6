#Exercise 2 Lottery Number Generator
import random

def generator():
    """Seven random numbers are put in a list and get displayed

    """
    try:
        lottery_num = []

        for digit in range(0,7):
            num = random.randint(0, 9)
            lottery_num += [num]

        for i in range(0,len(lottery_num)):
            print(lottery_num[i])
    except IOError:
        print("File can't be found")
    except IndexError:
        print("Index doesn't exist")
    except:
        print("Can't find the problem")
    

if __name__ == "__main__":
    generator()



#Exercise 4 Number Analysis Program
def num_analyser():
    """Asks the user to enter 20 numbers and adds them to the list
    and displays the min, max, total and average of the numbers in list
    """

    try:
        amount = 20

        numbers = [] * amount

        index = 0

        while index < amount:
            numbers += [int(input("Enter a number: "))]
            index +=1
        
        print(min(numbers))
        print(max(numbers))
        print(sum(numbers))
        print(sum(numbers) / 20)
    except ValueError:
        print("Conversion integer failed")
    except:
        print("Problem can't be found")

    
if __name__ == "__main__":
    num_analyser()


#Exercise 6 Dice Rolling Function
import random

def roll(number_of_throws):
    """A list is made of random numbers but first the amount of random numbers
    you want is entered

    Input:
    number_of_throws - int - number of random numbers you want

    Output:
    list_number - list - list with the random numbers
    
    """
    try: 
        list_number = []
        for i in range(number_of_throws):
            num = random.randint(1,6)
            list_number += [num]

        return print(list_number)
    except IOError:
        print("File can't be found")
    except:
        print("Problem can't be found")
    

if __name__ == "__main__":
  number_of_throws = int(input("Enter a positive number: "))
  roll(number_of_throws)
