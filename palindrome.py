import time

def  is_palindrome(val):
    val = str(val)
    if val == val[::-1]:
        return (True)
    else:
        return(False)
    

def palindrome():
    start_time = time.time()
    palindrome_list = []
    debug_list = []
    low_val = 900
    high_val = 999
    
    iterations = 0

    for num1 in range(low_val, high_val):
        for num2 in range(low_val, high_val):
            iterations += 1
            print(num1,  num2)
            if is_palindrome(num1*num2):
                palindrome_list.append(num1*num2)
                debug_list.append([num1,num2, num1*num2])

    print('print of palindromes:',palindrome_list, num1, num2)
    print('debug_list:', debug_list)
    print('Iterations:' , iterations)
    print('Largest palindrome:', max(palindrome_list) )
    print('Runtime: ', time.time() - start_time)
    print('--------end---------')

palindrome()