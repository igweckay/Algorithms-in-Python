#! /usr/bin/env python3

def happyBirthday():
    song='''Happy birthday to you! Happy birthday to you! Happy birthday dear Kay. Happy birthday to you!'''
    print(song)

#main####
happyBirthday()


def sumProblemString(x, y):
    sum = x + y
    return "The sum of {} and {} is {}.".format(x, y, sum)

def main():
    print(sumProblemString(2, 3))
    print(sumProblemString(1234567890123, 535790269358))
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    print(sumProblemString(a, b))

main()
