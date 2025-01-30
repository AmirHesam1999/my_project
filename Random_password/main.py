#!/usr/bin/python3

import random

characters = "'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'"
number = int(input("please enter the number of digits: "))
randomPassword = "".join(random.sample(characters,number))
print(randomPassword)
