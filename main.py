import re
from collections import OrderedDict

from student import Student


def check_password(passwords):
    """Returns a list of all acceptable passwords"""
    new_list = []
    for password in passwords:
        if 5 < len(password) < 13 and \
                re.findall("[A-Z]", password) and \
                re.findall("[a-z]", password) and \
                re.findall("[0-9]", password) and \
                re.findall("[$#@]", password):
            new_list.append(password)
    return new_list


def sort_list_by_name_age_score(list):
    """Sorts a list by name then age then score"""
    list_sorted = sorted(list, key=lambda i : (i[0], i[1], i[2]))
    return list_sorted


def find_numbers_divisible_by_seven(nums):
    """Finds numbers divisible by seven"""
    new_nums = []
    for n in nums:
        if n % 7 == 0:
            new_nums.append(n)
    return new_nums


def robot_moves(list):
    """Robot moves"""
    position_up_down = 0
    position_left_right = 0
    for l in list:
        if l[0] == "DOWN":
            position_up_down = position_up_down + (l[1] * -1)
        elif l[0] == "UP":
            position_up_down = position_up_down + l[1]
        elif l[0] == "LEFT":
            position_left_right = position_left_right + (l[1] * -1)
        elif l[0] == "RIGHT":
            position_left_right = position_left_right + l[1]
    return abs(position_up_down / position_left_right)


def compute_frequency_of_words(input):
    """Compute frequency of words"""
    output = {}
    temp = input.split()
    for t in temp:
        if t == "3?":
            x = t.replace(t, "3\?")
            output[t] = len(re.findall(x, input))
        else:
            output[t] = len(re.findall(t, input))
    output_sorted = OrderedDict(sorted(output.items()))
    return output_sorted


def calculate_square_of_a_number(num):
    """Calculate the square of a number"""
    return num**2


def display_some_doc_srings(num):
    """Display some doc strings"""
    if num == 1:
        print(abs.__doc__)
    elif num == 2:
        print(int.__doc__)
    elif num == 3:
        print(check_password.__doc__)

def class_vs_instiance_variables():
    """Difference between class variables and instance variables"""
    print("Student class has one class variable named school\n"
          "Two instance variables name and age\n"
          "After creating two objects, one with a name of Tucker age 25 and one with a name of Buddy age 15\n"
          "The class variable can be accessed by both instances and returns the same string 'My School'\n")
    st = Student("Buddy", 25)
    nt = Student("Tucker", 15)
    print(st.school)
    print(st.name)
    print(st.age)
    print("************")
    print(nt.school)
    print(nt.name)
    print(nt.age)


def compute_the_sum(a, b):
    """Calculate the sum of two numbers"""
    return a + b


if __name__ == '__main__':

    while True:
        print("===== Menu =====\n"
              "1 - Check a list of passwords\n"
              "2 - Sort a list by name then age then score\n"
              "3 - Find some numbers divisible by 7\n"
              "4 - Calculate robot moves\n"
              "5 - Compute the frequency of words in a string\n"
              "6 - Calculate the square of a number\n"
              "7 - Display some doc strings\n"
              "8 - Class vs Instance variables\n"
              "9 - Sum two numbers\n"
              "e  - Exit the program\n")
        selection = input("Choose from the menu")
        count = 0
        a_list = []
        if selection == "e":
            break
        elif selection == "1":
            print("Great! Let's build your list\n")
            size = input("Enter the size of your list")
            while count < int(size):
                item = input("Pleae enter a password")
                a_list.append(item)
                count += 1
            print("Perfect! Here are your passwords that passed the test:")
            for w in check_password(a_list):
                print(w)
            count = 0
            a_list.clear()
        elif selection == "2":
            print("Great! First we need your list. You will enter name, age and score for each entry")
            size = input("Enter the size of your list")
            while count < int(size):
                name = input("Enter a name")
                age = input("Enter the age")
                score = input("Enter a score")
                temp = (name, age, score)
                a_list.append(temp)
                count += 1
            my_sorted_list = sort_list_by_name_age_score(a_list)
            print(my_sorted_list)
            count = 0
            a_list.clear()
        elif selection == "3":
            print("Great! Check for numbers divisable by 7")
            size = input("Enter your list size")
            while count < int(size):
                num = input("Enter a number")
                a_list.append(int(num))
                count += 1
            print("Here is your numbers divisible by 7:\n")
            for n in find_numbers_divisible_by_seven(a_list):
                print(n)
            count = 0
            a_list.clear()
        elif selection == "4":
            print("Great! Calculate robot moves\nYou will enter UP, DOWN, LEFT, RIGHT followed by a number of spaces")
            size = input("Enter your number of moves")
            while count < int(size):
                direction = input("Enter a direction").upper()
                steps = input("Enter number of steps")
                temp = (direction, int(steps))
                a_list.append(temp)
                count += 1
            print("Calculating your location away from 0,0")
            print(robot_moves(a_list))
            count = 0
            a_list.clear()
        elif selection == "5":
            print("Great! Comput the frequency of words in a string")
            entry = input("Enter your string")
            for key, value in compute_frequency_of_words(entry).items():
                print(key + " : " + str(value))
        elif selection == "6":
            print("Great! Calculate the square of a number")
            num = input("Enter your number")
            print(calculate_square_of_a_number(int(num)))
        elif selection == "7":
            print("Great! Let's display some doc strings\n"
                  "1 - abs doc string\n"
                  "2 - int doc string\n"
                  "3 - check passwords doc string")
            doc_selection = input("Select a doc string")
            display_some_doc_srings(int(doc_selection))
        elif selection == "8":
            print("Great! You want to see my example of class and instances variables")
            class_vs_instiance_variables()
        elif selection == "9":
            print("Great! You want to see the sum of two numbers")
            num1 = input("Enter your first number")
            num2 = input("Enter your second number")
            print(compute_the_sum(int(num1), int(num2)))
