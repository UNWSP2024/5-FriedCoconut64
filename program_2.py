import math
import random


def main():
    global num1
    global num2
    num1 = random.randint(1,1000)
    num2 = random.randint(1,1000)

def random_quiz():
    print(num1)
    print('+',num2)
    print("-----")
    answer = float(input())
    return answer

main()
answer = random_quiz()
if answer == num1 + num2:
    print("Congratulations")
else:
    print('Good try, the correct answer is', num1 + num2)
