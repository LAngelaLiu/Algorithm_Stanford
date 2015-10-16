# Algorithm
# Week 1

# Karatsuba multiplication

# x = 10^(n/2) a + b
# y = 10^(n/2) c + d
# x * y = 10^n ac + 10^(n/2) (ad + bc) + bd


import time
import math


def get_input_int():
    '''
    Prompt user for an integer number.
    return the integer value for further use. 

    '''

    while True:
        x = input("Enter an integer number: ")
        #print(x)
        #print(len(x))
        try:
            int_x = int(x)
            return int_x
        except:
            print("Not a valid number. Try again.")

        #length = len(x)
        #half_index = int(length/2)
        #int_a = int(x[:half_index])
        #int_b = int(x[half_index:])
        #return int_x, length, int_a, int_b 


# avoid string casting
# use math-based manipulations to split an integer into two parts
def Karatsuba_multiply(x, y):
    # number of digits
    if x == 0 or y == 0:
        return 0
    
    num_digits_x = int(math.log10(x) + 1)
    num_digits_y = int(math.log10(y) + 1)
    
    if num_digits_x == 1 or num_digits_y == 1:
        #print(str_x, " * ", str_y, " = ", x * y )
        return x * y
    else:
        # keep x as the smaller number
        if num_digits_x > num_digits_y:
            temp = x
            x = y
            y = temp
            tmp_num = num_digits_x
            num_digits_x = num_digits_y
            num_digits_y = tmp_num

        half_length_x = int(num_digits_x / 2)
        power_x = num_digits_x - half_length_x  # power in equation
        # half block
        divider = 10**power_x
        a = int(x / divider)
        b = x % divider

        # for y
        # half_length_y = num_digits_y - power_x # same power as x
        c = int( y / divider )
        d = y % divider

        ac_term = Karatsuba_multiply(a, c)
        bd_term = Karatsuba_multiply(b, d)
        #print('a+b=', a+b)
        #print('c+d=', c+d)
        cross_term = Karatsuba_multiply(a+b, c+d)
        # product
        equation = divider**2 * ac_term + bd_term + \
                   divider * ( cross_term - ac_term - bd_term )
        #print('ac_term: ', ac_term)
        #print('bd_term: ', bd_term)
        #print('cross_term: ', cross_term) 
        #print( equation )
        return equation


    

def test_Karatsuba_multiply(upper_limit=int(1E10)):
    '''
    Loop over positive integers from 1 to 1 million.
    Perform Karatsuba multiplication and compare with
    regular multiplication.
    If the results are not equal, output error messages.
    
    '''

    num_error = 0
    for i in range(1, upper_limit):
        for j in range(1, upper_limit):
            prod = i * j
            prod_KM = Karatsuba_multiply(i, j)

            if prod != prod_KM:
                print('Error in recursive multiplication.')
                print('Correct Answer is: ', i, ' * ', j, ' = ', prod)
                print('Incorrectly computed as: ', prod_KM)
                num_error += 1

    print('Karatsuba implementation error for ', upper_limit, \
          '^2 multiplications has ', num_error, ' errors.')



    
def compute_time(KM=False, upper_limit=int(1E10)):
    # start time
    time_start = time.time()
    for i in range(1, upper_limit):
        for j in range(1, upper_limit):
            if KM:
                prod_KM = Karatsuba_multiply(i, j)
            else:
                prod = i * j

    # end time
    time_end = time.time()
    # elapsed time
    time_spent = time_end - time_start
    
    return time_spent


def test_input_multiply():
    '''
    Trial 1
    obtain two user input integers and do Karatsuba multiplication
       and compare with regular multiplication
    '''

    x = get_input_int()
    y = get_input_int()

    prod = Karatsuba_multiply(x, y)
    print(prod)

    if x * y != prod:
        print('Error in recursive multiplication.')
        print('Correct Answer is: ', x, ' * ', y, ' = ', x * y)


#test_input_multiply()


# Task 0
# do multiplication of all numbers from 1 to 1 million
# verify that the Karatsuba multiplication implementation is correct
#  by comparing with regular multiplication
test_Karatsuba_multiply(int(1E3))
#test_Karatsuba_multiply(int(1E5))
#test_Karatsuba_multiply(int(1E6))

#quit()


# Task 1
# compare regular multiplication and Karatsuba multiplication
# running time

for i in range(2, 10):
    upper_limit = int(10**i)
    print('Maximum value: ', upper_limit)
    regular_RT = compute_time(False, upper_limit)
    print('Regular multiplication running time: ', regular_RT)
    K_RT = compute_time(True, upper_limit)
    print('Karatsuba multiplication running time: ', K_RT)



quit()


# Trials and tests


# Trial 0
# Easy case
# assume x and y are both N-digit numbers and N is an even number

x, N_x, a, b = get_input_int()
y, N_y, c, d = get_input_int()

if N_x == N_y and N_x % 2 == 0:
    half_digit = N_x / 2

    product = x * y
    product_2 = a * c * 10**N_x + ( a * d + b * c ) * 10**(N_x/2) + b * d

    print(product, product_2)
    if product != product_2:
        print('Error: multiplication error.')
        

# assume positive integers
# string casting is roughly the same running time as the math-based routine
# need to work on when x and y have different number of digits
def recursive_multiply(x, y):
    str_x = str(x)
    str_y = str(y)
    # assume len(str_x) == len(str_y) for simple cases
    if len(str_x) == 1 or len(str_y) == 1:
        #print(str_x, " * ", str_y, " = ", x * y )
        return x * y
    else:
        length_x = len(str_x)
        length_y = len(str_y)

        # keep x as the smaller number
        if length_x > length_y:
            temp = str_x
            str_x = str_y
            str_y = temp

        length_x = len(str_x)
        half_length_x = int(length_x / 2)
        power_x = length_x - half_length_x  # power in equation
        # half block
        a = int( str_x[:half_length_x] )
        b = int( str_x[half_length_x:] )
        # for y
        length_y = len(str_y)
        half_length_y = length_y - power_x # same power as x
        c = int( str_y[:half_length_y] )
        d = int( str_y[half_length_y:] )

        ac_term = recursive_multiply(a, c)
        bd_term = recursive_multiply(b, d)
        #print('a+b=', a+b)
        #print('c+d=', c+d)
        cross_term = recursive_multiply(a+b, c+d)
        # product
        equation = 10**(2*power_x) * ac_term + bd_term + \
                   10**power_x * ( cross_term - ac_term - bd_term )
        #print('ac_term: ', ac_term)
        #print('bd_term: ', bd_term)
        #print('cross_term: ', cross_term) 
        #print( equation )
        return equation
   



        
