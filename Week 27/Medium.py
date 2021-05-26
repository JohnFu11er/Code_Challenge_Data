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
    # return
    print(range20_comp())
    print(range20_simple())
    print(range100_comp())
    print(range100_simple())

def range20_comp():
    ''' returns a list of odd numbers from 1 - 20 '''
    return [i for i in range(1,21,2)]


def range20_simple():
    ''' returns a list of odd numbers from 1 - 20 '''
    # function
    _temp = list()
    for i in range(1,21,2):
        _temp.append(i)
    return _temp

def range100_comp():
    ''' All even numbers in a range of 100
    that are both divisible by 2 and 5.'''
    return [i for i in range(0,101,2) if i % 5 == 0]

def range100_simple():
    ''' All even numbers in a range of 100
    that are both divisible by 2 and 5.'''
    _data = list()
    for i in range(0,101,2):
        if i % 5 == 0: 
            _data.append(i)
    return _data

if __name__ == "__main__":
    main()