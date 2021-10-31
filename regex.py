import re
def init_regex():
    whitespace = re.compile(r'(\s)+')
    cout = re.compile(r'cout')
    out_oper = re.compile(r'\<\<')
    class_func = re.compile(r'class')
    function = re.compile(r'[_a-zA-Z][a-zA-Z0-9_]*\(')
    logic_state = re.compile(r'true|false')
    definition = re.compile(r'(\_|[a-zA-Z])([a-zA-Z0-9]|\_)*')
    math_type = re.compile(r'int|float|string')
    array = re.compile(r'(\_|[a-zA-Z])([a-zA-Z0-9]|\_)*\[(\_|[a-zA-Z])([a-zA-Z0-9]|\_)*\]')
    bool_type = re.compile(r'bool')
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
    comment = re.compile(r'(//(.)*\n)|(\/\*(.)*\*\/)', re.DOTALL)
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
    dicts['comment'] = comment
    dicts['array'] = array
    dicts['cout'] = cout
    dicts['out_oper'] =out_oper
    dicts['if_key'] = if_key
    dicts['else_key'] = else_key
    dicts['for_key'] = for_key
    dicts['while_key'] = while_key
    dicts['return_key'] = return_key
    dicts['math_type'] = math_type
    dicts['bool_type'] = bool_type
    dicts['logic_state'] = logic_state
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

