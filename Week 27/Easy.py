''' 
EASY
Create a list comprehension to return the alphabet as a list. Provide a basic for loop as well as the list comprehension; for comparative purposes
'''

# Define vars
alpha = "abcdefghijklmnopqrstuvwxyz"

def main():
    print(alpha_comp(alpha))
    print(alpha_for_loop(alpha))

def alpha_comp(data: str):
    ''' Returns a list of all items from a string argument '''
    return [ i for i in data]

def alpha_for_loop(data: str):
    ''' Returns a list of all items from a string argument '''
    _temp = list()
    for i in data:
        _temp.append(i)
    return _temp

if __name__ == "__main__":
    main()