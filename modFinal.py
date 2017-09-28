#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 20:51:25 2017

@author: hans
"""

def get_names():
    i = 0
    names = []
    while i < 5:
        userIn = input("Enter the name of an element: ").strip().lower()
        if userIn == "":
            print("Please do not enter nothing.")
        elif userIn in names:
            print(userIn, "was already entered.")
        else:
            names.append(userIn)
            i += 1

    return names

def getFile():
    #!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt
    elementFile = open("elements1_20.txt", "r")
    elementList = []
    i = 0
    while i < 20:
        elementList.append(elementFile.readline().strip().lower())
        i += 1

    elementFile.close()
    return elementList

def compare():
    correct = []
    for element in elementList:
        i = 0
        while i < len(names):
            if element == names[i]:
                correct.append(names.pop(i))
            i += 1
    return correct

def getScore():
    return (len(correctList) / 5) * 100

def toString(list):
    string = ""
    for item in list:
        string = string + item + " "
    return string

print("list any 5 of the first 20 elements in the Period table")
elementList = getFile()
names = get_names()
correctList = compare()
percentCorrect = getScore()
found = toString(correctList)
notFound = toString(names)
print(int(percentCorrect), "% correct")
print("found:", found.title())
print("Not Found:", notFound.title())