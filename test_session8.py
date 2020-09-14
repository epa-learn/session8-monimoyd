import pytest
import random
import string
import session8
import os
import inspect
import re
import math
import collections


README_CONTENT_CHECK_FOR = [
'check_func_doc_string',
'function_less_doc_comments',
'function_less_doc_comments',
'next_fibonacci_num',
'func_calls_dict',
'count_function_calls_global_dict',
'add',
'mul',
'div',
'count_function_calls_local_dict'
]

# with pytest.raises(ValueError):

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 5
    
def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    missing = []
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            missing.append(c)
            #pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file" + str(missing)

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"  

		
def test_check_func_doc_string_less_than_50char_comment():
    ''' 
    This method tests check_func_doc_string with less than 50 character comments returning False
    '''
    assert session8.check_func_doc_string(session8.function_less_doc_comments) == False

def test_check_func_doc_string_more_than_50char_comment():
    ''' 
    This method tests check_func_doc_string with less than 50 character comments returning False
    '''
    assert session8.check_func_doc_string(session8.function_more_doc_comments) == True
		
	
def test_next_fibonacci_num():
    '''
    Test to next_fibonacci_num works
    '''
    result = []
	
    next_fib_num = session8.next_fibonacci_num()
    result.append(next_fib_num())
    result.append(next_fib_num())
    result.append(next_fib_num())
    result.append(next_fib_num())
    result.append(next_fib_num())
    result.append(next_fib_num())
    result.append(next_fib_num())
    result.append(next_fib_num())
    assert result == [ 0, 1, 1, 2, 3, 5, 8, 13]
	
def test_count_function_calls_global_dict():
    '''
    Test count_function_calls_global_dict works
    '''
    func_call_add = session8.count_function_calls_global_dict(session8.add)
    func_call_mul = session8.count_function_calls_global_dict(session8.mul)
    func_call_div = session8.count_function_calls_global_dict(session8.div)

    func_call_add(2, 3)
    func_call_add(2, 5)
    func_call_mul(1, 10)
    func_call_div(5, 3)
    func_call_div(3, 2)
    func_call_div(1, 10)
    assert session8.func_calls_dict["add"] == 2
    assert session8.func_calls_dict["mul"] == 1
    assert session8.func_calls_dict["div"] == 3
	
def test_count_function_calls_global_dict_unsupported_method():	
    '''
    Test count_function_calls_global_dict raises error when any method other than add, mul, div is called
    '''
    with pytest.raises(ValueError):
       session8.count_function_calls_global_dict(session8.sub) 
	
	
def test_count_function_calls_local_dict():
    '''
    Test count_function_calls_local_dict works
    '''
    user1_func_call_dict = collections.Counter()
    user1_func_call_add = session8.count_function_calls_local_dict(session8.add, user1_func_call_dict)
    user1_func_call_mul = session8.count_function_calls_local_dict(session8.mul, user1_func_call_dict)
    user1_func_call_div = session8.count_function_calls_local_dict(session8.div, user1_func_call_dict)

    user1_func_call_add(2, 3)
    user1_func_call_add(2, 5)
    user1_func_call_mul(1, 10)
    user1_func_call_div(5, 3)
    user1_func_call_div(3, 2)
    user1_func_call_div(1, 10)
	
    assert user1_func_call_dict["add"] == 2
    assert user1_func_call_dict["mul"] == 1
    assert user1_func_call_dict["div"] == 3
	
    user2_func_call_dict = collections.Counter()
    user2_func_call_add = session8.count_function_calls_local_dict(session8.add, user2_func_call_dict)
    user2_func_call_mul = session8.count_function_calls_local_dict(session8.mul, user2_func_call_dict)
    user2_func_call_div = session8.count_function_calls_local_dict(session8.div, user2_func_call_dict)

    user2_func_call_add(1, 12)
    user2_func_call_mul(5, 15)
    user2_func_call_mul(6, 23)
    user2_func_call_div(-1, 18)
    assert user2_func_call_dict["add"] == 1
    assert user2_func_call_dict["mul"] == 2
    assert user2_func_call_dict["div"] == 1
	

def test_count_function_calls_lcoal_dict_unsupported_method():	
    '''
    Test count_function_calls_global_dict raises error when any method other than add, mul, div is called
    '''
    with pytest.raises(ValueError):
        session8.count_function_calls_local_dict(session8.sub, {}) 

	

	
	
