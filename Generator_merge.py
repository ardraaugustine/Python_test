
""" Author = Ardra Augustine
    Email: ardraaugustine18@gmail.com   """


def merge(*args):
    Merge = sorted(iterable1+iterable2+iterable3, reverse=False)

    print("Merge sequence =", Merge)

if __name__ == '__main__':

    num1 = [9, 1, 5]
    iterable1= sorted(num1)
    print("Iterable 1 = ", iterable1)

    num2 = [5, 2]
    iterable2= sorted(num2)
    print("Iterable 2 = ", iterable2)

    num3 = [11, 1, 10, 6]
    iterable3= sorted(num3)
    print("Iterable 3 = ", iterable3, '\n')
    merge(iterable1, iterable2, iterable3)

""" 
OUTPUT: 
Iterable 1 =  [1, 5, 9]
Iterable 2 =  [2, 5]
Iterable 3 =  [1, 6, 10, 11]

Merge sequence = [1, 1, 2, 5, 5, 6, 9, 10, 11]

"""    
