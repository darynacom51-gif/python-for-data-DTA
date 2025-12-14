import random   # random.randrange(5)
# import random as r  # r.randrange(5)
# from random import * # randrange(5)
# # from numpy import *
# from random import randrange, randint # randrange(5)
# from random import randrange as rr #rr(5)

#   пишемо консольну гру

comp_choice = random.randint(0,100) # задали діапазон загаданого числа
n_count = 0
while n_count < 3:
    try:
        user_choice = int(input("Enter your number: "))
    except ValueError:
        print("Uncorrect number!")
        continue
    else:
        print("Excelent! I remember your number")

    finally:
        n_count += 1
        print(f"Your attempt {n_count}")
    if user_choice == comp_choice:
        print("Congratulations")
        break
    print("Try again!")
