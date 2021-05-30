'''
MEDIUM
Create a conditional and a nested list comprehension to return 
    1.) All odd numbers in a range of 20
    2.) All even numbers in a range of 100 that are both divisible by 2 and 5.
As with the easy challenge, provide a basic for loop as well as the list comprehension for comparative purposes. 

Example
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
'''

def main():
    range_high = int(input("Enter the highest number of the range: "))
    divisors = input("Enter test divisors seperated by commas: ").split(",")
    print(medium_combined(range_high, divisors))
    

def divisor_test(num, divisors):
    ''' Returns bool for divisor test'''
    for divisor in divisors:
        if num % int(divisor) != 0:
            return False
    return True


def medium_combined(top: int, divisors: list):
    ''' Returns a list of numbers that are divisable
    by all numbers in the divisor list '''
    data = list()
    for num in range(1,top + 1):
        if divisor_test(num, divisors):
            data.append(num)
                
    return data


if __name__ == "__main__":
    main()