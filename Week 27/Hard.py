'''
HARD

The aliquot sum of a number is the sum of the factors of that number, not including itself. 

Example: 
The factors of 6 are: 1, 2, 3, 6. Not including the number itself: 1+2+3=6
The factors of 20 are: 1, 2, 4, 5, 10, 20. Not including the number itself: 1+2+4+5+10=22
The factors of 8 are: 1, 2, 4, 8. Not including the number itself: 1+2+4=7

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
'''


def main():
    user_low = int(input("Enter the lowest number to test for aliquot numbers: "))
    user_high = int(input("Enter the highest number to test for aliquot numbers: "))
    for item in aliquot_lists(user_low, user_high):
        print(item)


def aliquot_lists(user_low: int, user_high: int):
    ''' Returns three lists of numbers according
    to their status as an aliquot number
    
    - Perfect: sum of factors = number
    - Abundant: sum of factors > number
    - Deficient: sum of factors < number
    '''
    
    data = [aliquot_determination(i) for i in range(user_low, user_high + 1)]
    perfect_list = [i[0] for i in data if i[1] == "perfect"]
    abundant_list = [i[0] for i in data if i[1] == "abundant"]
    deficient_list = [i[0] for i in data if i[1] == "deficient"]
    
    return [
        f'Perfect Numbers {perfect_list}',
        f'Abundant Numbers {abundant_list}',
        f'Deficient Numbers {deficient_list}'
    ]
    

def is_factor(num, divisor):
    ''' Returns bool for given divisor
    
    - True: is a factor
    - False: not a factor
    '''
    
    if num % divisor == 0:
        return True
    return False


def aliquot_determination(num: int):
    ''' Returns number given as argument
    and the determination of its aliquot
    number status
        
    - Perfect: sum of factors = number
    - Abundant: sum of factors > number
    - Deficient: sum of factors < number
    '''
    
    divisors = list()
    factors = [divisor for divisor in range(1,num) if is_factor(num,divisor)]
    factors_sum = sum(factors)
    if factors_sum < num:
        aliquot = "deficient"
    elif factors_sum > num:
        aliquot = "abundant"
    else:
        aliquot = "perfect"

    return [num, aliquot]


if __name__ == "__main__":
    main()