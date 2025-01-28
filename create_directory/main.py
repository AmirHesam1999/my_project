#!/bin/python3
import os

path = input("Please enter new path: ")
os.chdir(path)

name = input("Please enter name file : ")
os.mkdir(name)
