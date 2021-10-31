import re
from automat import init_automat
from regex import init_regex


def check_automat(automat, stack, buffers, count = 0):
    if(stack == ['$']):
        if(len(buffers)==0):
            return True
        return False
    # if count >20:
    #     return False
    if len(stack) > len(buffers) + 1:
        # print('Noway')
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
                if key[0] == token:
                    count = count + 1
                    new_stack = stack.copy()
                    new_stack.pop(0)
                    for i in range(len(key[1]) - 1, -1, -1):
                        new_stack.insert(0, key[1][i])
                    
                    check = check or check_automat(automat, new_stack, buffers, count)
            return check
        else:
            if token == buffers[0]:
                new_stack = stack.copy()
                # print(str(len(stack))+token)
                new_stack.pop(0)
                # print(str(len(buffers))+ token+' '+ token)
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
    for key in list_token.keys():
        print(str(key)+" "+str(list_token[key]))
    # print(list_token)
    stack = ['Global', '$']
    buffers = []
    automat = init_automat()
    for token in list_token.values():
        buffers.append(token)
    while 'whitespace' in buffers:
        buffers.remove('whitespace')
    # for token in buffers:
    #     print(token)
    result = check_automat(automat, stack, buffers)
    print(result) 


    

main()







    
