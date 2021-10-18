import re
f = open('sample.txt', 'r', encoding='UTF-8')
text = f.read()
whitespace = re.compile(r'[\s]]+')
indentifier = re.compile(r'[_a-zA-Z][a-zA-Z0-9_]*')
keyword = re.compile(r'boolean|break|continue|else|for|float|if|int|return|for|while')
int_lit = re.compile(r'[0-9]+')
float_lit = re.compile(r'[0-9]+|([0-9]+\.[0-9]*)|(\.[0-9]+)')
library = re.compile(r'\#include<[0-9a-zA-Z\.\+]+>')

arithmetic_operators = re.compile(r'\+|\-|\*|\/|\=\=')
relational_operators = re.compile(r'\>|\>\=|\<\=|\<')
equal_operators = re.compile(r'\=\=|\!\=')
logical_operators = re.compile(r'\&\&|\|\||\!')
assignment_operators = re.compile(r'\=')
print(library.match('#include<bh>'))
end_cmd = re.compile(r'\;')

dict = {}
dict['whilespace'] = whitespace;
dict['indentifier'] = indentifier
dict['keyword'] = keyword
dict['int_lit'] = int_lit
dict['float_lit'] = float_lit
dict['library'] = library
dict['arithmetic_operators'] = arithmetic_operators
dict['relational_operators'] = relational_operators
dict['equal_operators'] = equal_operators
dict['logical_operators'] = logical_operators
dict['assignment_operators'] = assignment_operators
dict['end_cmd'] = end_cmd


# def scan(text, start, current, list_type_valid, check_end, list_token):
#     if current == len(text): return list_token
#     if(check_end == False):
#         list_type_valid_current = []
#         for category in list_type_valid:
#             if dict[category].fullmatch(text[start:current+1]) != None:
#                 list_type_valid_current.append(category)
#         if(len(list_type_valid_current) == 0):
#             check_end = True
#             token = []
#             token.append(text[start:current])
#             for category in list_type_valid:
#                 token.append(category)
#             start = current
#             list_token.append(token)
#         else: 
#             current = current + 1
#         return scan(text, start, current, list_type_valid_current, check_end, list_token)
#     else: 
#         check_end = False
#         list_type_valid = []
#         for category in dict.keys():
#             if dict[category].fullmatch(text[start:current+1]) != None:
#                 list_type_valid.append(category)
#         if len(list_type_valid) == 0: 
#             print('[ ' +text[start:current+1] + ' ]'+ " at position" + str(start) +"is not found")
#             start = start + 1
#             current = current + 1
#             check_end = True
#             return scan(text, start, current, list_type_valid, check_end, list_token)
#         else:
#             return scan(text, start, current + 1, list_type_valid, check_end, list_token)

def scan(text, current, list_token):
    if current == len(text):
        return list_token
    list_type_valid = {}
    for category in dict.keys():
        if dict[category].search(text[current:]) != None:
            list_type_valid[category] = dict[category].search(text[current: len(text)]).start() + current
    if len(list_type_valid) > 0:
        list_index = []
        for key in list_type_valid:
            list_index.append(list_type_valid[key])
        index_must_find = min(list_index)
        if index_must_find != current:
            token = []
            token.append(text[current:index_must_find])
            token.append("cannot be defined")
            list_token.append(token)
        category_must_find = ''
        current = index_must_find
        for key in list_type_valid:
            if list_type_valid[key] == index_must_find:
                category_must_find = key
                break
        stop = current
        while dict[category_must_find].fullmatch(text[current:stop+1]) == None:
            stop = stop + 1
        while dict[category_must_find].fullmatch(text[current:stop+1]) != None:
            stop = stop + 1
        Token = []
        Token.append(text[current:stop])
        Token.append(category_must_find)
        list_token.append(Token)
        current = stop
        return scan(text, current, list_token)
    else:
        Token = []
        Token.append(text[current:len(text)])
        Token.append("cannot be defined")
        list_token.append(Token)
        return list_token




def main():
    f = open('sample.txt', 'r', encoding='UTF-8')
    text = f.read() 
    print(len(text))
    print(scan(text, current=0,  list_token=[]))

main()







    
