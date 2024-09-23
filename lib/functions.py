#!/usr/bin/env python3

# Define a method greet_programmer() that takes no arguments and prints "Hello, programmer!"
def greet_programmer():
    print("Hello, programmer!")

# Define a method greet() that takes one argument, name, and prints "Hello, name!"
def greet(name):
    print(f"Hello, {name}!")

# Define a method greet_with_default() that takes one argument, name. 
# If no argument is passed, it defaults to "programmer"
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# Define a method add() that takes two numbers as arguments and returns their sum
def add(num1, num2):
    return num1 + num2

# Define a method halve() that takes one number and returns its value divided by two
def halve(number):
    return number / 2

greet_programmer()
greet("Alice")
greet_with_default()
print(add(5, 3))
print(halve(10))