# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 09:55:14 2024

@author: UOD Student
"""

num1 = input ("Please insert the first number: ")
num2 = input ("Please insert the second number: ")

operation = input ("Please insert your desired operation among: +, -, *, /: ")

if operation == "+":
    result = float(num1) + float(num2)
    
if operation == "-":
    result = float(num1) - float(num2)
    
if operation == "*":
    result = float(num1) * float(num2)
    
if operation == "/":
    result = float(num1) / float(num2)
    
print ("the result is: ", result)