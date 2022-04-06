import math

question = {"What would you like to calculate? "}
options = [["1.Sqrt","2.Log","3.Factorial"]]

Fun = []
Fun_num = 1

for key in question:
        print("-------------------------")
        print(key)
        for i in options[Fun_num-1]:
            print(i)
        guess = input("Enter (1, 2, 3): ")
        guess = guess.upper()
        Fun.append(guess)
# # -------------------------
def check_answer(guess):

    if guess == "1":
        number_to_cla = int(input("Enter the number to sqrt:"))
        print(math.sqrt(number_to_cla))
    elif guess == "2":
        number_tow_to_cal = int(input("Enter the number to log:"))
        print(math.log(number_tow_to_cal))
    elif guess == "3":
        number_three_to_cal = int(input("Enter the number to factorial:"))
        print(math.factorial(number_three_to_cal))
    else:
        print("pleas select from 1 to 3")
# # -------------------------
check_answer(guess)