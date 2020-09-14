import random
import math
import time
import itertools
import collections
import functools


def check_func_doc_string(func: 'Function')->bool:
    ''' 
    This method checks whether the passed function has docstring greater than 50 characters
    '''
    min_number_of_docstring = 50
    def inner()->bool:
        '''
        This function determines if passed function has at least 50 characters
		'''
        if len(func.__doc__) < min_number_of_docstring:
            return False
        else:
            return True
    return inner()	
			
def function_less_doc_comments(a, b):
    ''' Test < 50 char comments '''
    return a+b
	
def function_more_doc_comments(a, b):
    ''' 
	This is a test function for showing more than 50 characters in documentation comments. It takes two parameters
	a and b and returns the value for a -b
	'''
    return a - b

def next_fibonacci_num()->int:
    '''
    This method return the next fibonacci number
    :return: next fibonacci number
    '''
    prev_fib = 0
    cur_fib = 1
    counter = -1
    def get_fib():
        nonlocal counter,prev_fib, cur_fib
        counter += 1
        if counter == 0:
            return 0
        elif counter == 1:
            return 1
        else:
            temp = prev_fib + cur_fib
            prev_fib = cur_fib
            cur_fib = temp
        return cur_fib
    return get_fib
	
def add(a, b):
    '''
	This function returns summation of two parameters a and b 
	'''
    return a + b

def mul(a, b):
    ''' 
    This function returns result of multiplication of parameters a and b
    '''
    return a * b

def div(a, b):
    ''' 
    This function returns result of division of parameter a by b
    '''
    return a/b
	
def sub(a, b):
    ''' 
    This function returns result of subtraction of parameter b from a
    '''
    return a-b


## Global dictionary which will keep track of how mnay times methods add, mul, div is called
func_calls_dict = collections.Counter()

def count_function_calls_global_dict(func: 'Function')->bool:
    '''
    This method updates a global dictionary func_calls_dict, how many times methods add,mul, div are called
    '''
    min_number_of_docstring = 10
    def inner_count_tracker(*args, **kwargs):
        '''
        This function tracks how many times function is called
		'''
        global func_calls_dict
        func_calls_dict[func.__name__] += 1
        return func(*args, **kwargs)
    if func.__name__ not in ["add", "mul", "div"]:
        raise ValueError("Only function add, mul, div can be passed to the function count_function_calls_global_dict")
	
    return inner_count_tracker


def count_function_calls_local_dict(func: 'Function', func_calls_dict={})->bool:
    '''
    This method updates a dictionary passed as parameter to teh fuction to keep track of 
    how many times methods add,mul, div are called
    '''
    def inner_count_tracker(*args, **kwargs):
        '''
        This function tracks how many times function is called
		'''
        nonlocal func_calls_dict
        func_calls_dict[func.__name__] += 1
        return func(*args, **kwargs)
		
    if func.__name__ not in ["add", "mul", "div"]:
        raise ValueError("Only function add, mul, div can be passed to the function count_function_calls_global_dict")
    return inner_count_tracker

