import re
from automat import init_automat
f = open('sample.txt', 'r', encoding='UTF-8')
def init_regex():
    text = f.read()
    whitespace = re.compile(r'(\s)+')
    cout = re.compile(r'cout')
    out_oper = re.compile(r'\<\<')
    class_func = re.compile(r'class')
    function = re.compile(r'[_a-zA-Z][a-zA-Z0-9_]*\(')
    definition = re.compile(r'(\_|[a-zA-Z])([a-zA-Z0-9]|\_)*')
    math_type = re.compile(r'int|float|string')
    bool_type = re.compile(r'boolean')
    break_key = re.compile(r'break')
    continue_key = re.compile(r'continue')
    if_key = re.compile(r'if')
    else_key = re.compile(r'else')
    for_key = re.compile(r'for')
    while_key = re.compile(r'while')
    return_key = re.compile(r'return')
    int_lit = re.compile(r'[0-9]+')

    float_lit = re.compile(r'[0-9]+|([0-9]+\.[0-9]*)|(\.[0-9]+)')
    library = re.compile(r'\#include<[0-9a-zA-Z\.\+]+>')
    standard = re.compile(r'using namespace std')
    string_lit = re.compile(r'\"(.)*\"', re.DOTALL)
    add_assign = re.compile(r'\+\=')
    oper_assign = re.compile(r'\-\=|\*\=|\/\=')
    add_oper = re.compile(r'\+')
    double_arithmetic_operators = re.compile(r'\+\+|\-\-')
    arithmetic_operators = re.compile(r'\-|\*|\/')
    relational_operators = re.compile(r'\>|\>\=|\<\=|\<')
    equal_oper = re.compile(r'\=\=|\!\=')
    logical_operators = re.compile(r'\&\&|\|\|')
    single_logical_operators = re.compile(r'\!')
    equal_assign = re.compile(r'\=')
    print(library.match('#include<bh>'))
    end_cmd = re.compile(r'\;')
    comment = re.compile(r'//(.)*\n')
    start_inner_cmd = re.compile(r'\{')
    end_inner_cmd = re.compile(r'\}')
    start_oper = re.compile(r'\(')
    end_oper = re.compile(r'\)')
    comma = re.compile(r'\,')


    dicts = {}

    dicts['library'] = library
    dicts['standard'] = standard
    dicts['break_key'] = break_key
    dicts['continue_key'] = continue_key
    dicts['cout'] = cout
    dicts['out_oper'] =out_oper
    dicts['if_key'] = if_key
    dicts['else_key'] = else_key
    dicts['for_key'] = for_key
    dicts['while_key'] = while_key
    dicts['return_key'] = return_key
    dicts['math_type'] = math_type
    dicts['bool_type'] = bool_type
    dicts['class_func'] = class_func
    dicts['function'] = function
    dicts['end_oper'] = end_oper

    dicts['definition'] = definition
    dicts['comma'] = comma

    dicts['start_inner_cmd'] = start_inner_cmd
    dicts['end_inner_cmd'] = end_inner_cmd

    dicts['int_lit'] = int_lit
    dicts['float_lit'] = float_lit
    dicts['string_lit'] = string_lit
    dicts['start_oper'] = start_oper
    dicts['add_assign'] = add_assign
    dicts['oper_assign'] = oper_assign
    
    dicts['double_arithmetic_operators'] = double_arithmetic_operators
    dicts['add_oper'] = add_oper
    dicts['arithmetic_operators'] = arithmetic_operators
    dicts['relational_oper'] = relational_operators
    dicts['equal_oper'] = equal_oper
    dicts['single_logical_operators'] = single_logical_operators
    
    dicts['logical_operators'] = logical_operators
    dicts['equal_assign'] = equal_assign
    dicts['end_cmd'] = end_cmd
    dicts['whitespace'] = whitespace;
    return dicts



def check_automat(automat, stack, buffers, count = 0):
    if(stack == ['$']):
        if(len(buffers)==0):
            return True
        return False
    if len(stack) > len(buffers) + 1:
        return False
    if len(buffers) > 0:
        token = stack[0];
        if token != token.lower():
            check = False
            list_valid = []
            for key in automat:
                if key[1][0] == buffers[0]:
                    list_valid.append(key[0])
            if len(list_valid) == 0:
                return False
            list_valid = sorted(set(list_valid))
            for key in automat:
                if key[0] == token and (key[1][0] == buffers[0] or key[1][0] in list_valid):
                    new_stack = stack.copy()
                    new_stack.pop(0)
                    for i in range(len(key[1]) - 1, -1, -1):
                        new_stack.insert(0, key[1][i])
                    
                    check = check or check_automat(automat, new_stack, buffers, count)
            return check
        else:
            if token == buffers[0]:
                new_stack = stack.copy()
                print(str(len(stack))+token)
                new_stack.pop(0)
                print(str(len(buffers))+ token+' '+ token)
                new_buffers = buffers.copy()
                new_buffers.pop(0)
                count = count + 1
                return check_automat(automat, new_stack, new_buffers, count)
            else:
                return False

    return False

                    

    
    
def scan(dicts, text, current, list_token):
    if current == len(text):
        return list_token
    list_type_valid = {}
    for category in dicts.keys():
        if dicts[category].search(text[current:]) != None:
            list_type_valid[category] = dicts[category].search(text[current: len(text)]).start() + current
    if len(list_type_valid) > 0:
        list_index = []
        for key in list_type_valid:
            list_index.append(list_type_valid[key])
        index_must_find = min(list_index)
        
        if index_must_find != current:
            list_token = add_list(list_token, text[current:index_must_find], current, 'cannot be defined')
        #     if text[current:index_must_find] in list_token.keys():
        #         list_token[[text[current:index_must_find], current]] = 'cannot be defined'

        category_must_find = ''
        current = index_must_find
        for key in list_type_valid:
            if list_type_valid[key] == index_must_find:
                category_must_find = key
                break
        stop = current
        while dicts[category_must_find].fullmatch(text[current:stop+1]) == None:
            stop = stop + 1
        while stop < len(text) and dicts[category_must_find].fullmatch(text[current:stop+1]) != None:
            stop = stop + 1
        
        list_token = add_list(list_token, text[current:stop], current, category_must_find)
                    

        current = stop
        return scan(dicts, text, current, list_token)
    else:
        list_token = add_list(list_token, text[current:len(text)], current, 'cannot be defined')
        return list_token

def add_list(list_token, string, current, label):
    list_token[string, current] = label
    return list_token


def same_scope(string, position_1, position_2):
    return False

def main():
    f = open('sample.txt', 'r', encoding='UTF-8')
    text = f.read() 
    text = text + '\n'
    print(len(text))
    dicts = init_regex()
    
    list_token = scan(dicts, text, current=0,  list_token={})
    for key in list_token.values():
        print(str(key)+" "+"1")
    # print(list_token)
    stack = ['Global', '$']
    buffers = []
    automat = init_automat()
    for token in list_token.values():
        buffers.append(token)
    while 'whitespace' in buffers:
        buffers.remove('whitespace')
    for token in buffers:
        print(token)
    result = check_automat(automat, stack, buffers)
    print(result) 


    

main()







    
