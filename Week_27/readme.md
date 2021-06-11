# Week 27 code review
<br>

## EASY
Create a list comprehension to return the alphabet as a list
    Provide a basic for loop as well as the list comprehension; for comparative purposes


### Example
alphabet = 'abcdefghijklmnopqrstuvwxyz'
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
<br><br>


## MEDIUM
Create a conditional and a nested list comprehension to return 
### 1.) All odd numbers in a range of 20
### 2.) All even numbers in a range of 100 that are both divisible by 2 and 5.
As with the easy challenge, provide a basic for loop as well as the list comprehension; for comparative purposes 


### Example
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]


## HARD


The aliquot sum of a number is the sum of the factors of that number, not including itself. 
## Example: 
The factors of 6 are: 1, 2, 3, 6. Not including the number itself: 1+2+3=6<br>
The factors of 20 are: 1, 2, 4, 5, 10, 20. Not including the number itself: 1+2+4+5+10=22<br>
The factors of 8 are: 1, 2, 4, 8. Not including the number itself: 1+2+4=7<br>


A "Perfect Number" is a number whose aliquot sum is equal to the number itself  (6 is a perfect number)
An "Abundant Number" is a number who aliquot sum is greater than the number itself (20 is an abundant number)
A "Deficient Number" is a number who aliquot sum is less than the number itself (8 is a deficient number)


Write a Python program that returns whether a number is perfect, abundant, or deficient from a given range. 
Append each number to a new list labeled "Perfect" "Abundant" and "Deficient"
Use list comprehension where possible. 

Example
Perfect Numbers ['6', '28', '496']
Abundant Numbers ['12', '18', '20']
Deficient Numbers ['1', '2', '3']