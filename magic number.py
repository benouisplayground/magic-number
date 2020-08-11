import random 

def ask_user_and_check_number():
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        print("You got the number right")
    if user_number not in magic_numbers:
        print("You didn't quite get it")
        
magic_numbers = [random.randint(0, 9), random.randint(0, 9)]
print(magic_numbers)

user_attemps = int(input("Enter the number of attempt: "))

def run_program_x_times(chances):
    for attempt in range(chances): #range(chances) is [0, 1, 2]
        print("This is attempt {}".format(attempt + 1))
        ask_user_and_check_number()

run_program_x_times(user_attemps)
    
