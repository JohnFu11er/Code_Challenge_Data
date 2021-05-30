'''
MEDIUM

Alternate solution for part 2 that allows the user to select
the range of numbers to test, and the divisors to test for.

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