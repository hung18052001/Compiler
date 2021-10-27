from main import scan

bracket = "([{)]}"
libBracket = ['function','start_inner_open','start_inner_cmd','end_inner_oper_or_end_func','end_inner_cmd']

def checkLinesOfBracket(s,lines):
    stack = []
    errindex = []
    n = len(s)
    # s = "[]{}[}[][}[}[][][{{{{{}{]{}{}{}[}[}[}{}{}{]{(()]}))))}}])})]]])]"
    for i in range(n):
        c = s[i]
        l = lines[i]
        if (c == '(' or c == '[' or c == '{'):
            # store a bracket as well as its index
            stack.append(l)
            stack.append(c)
        if (c == ')' or c == ']' or c == '}'):
            openbracket = bracket[bracket.index(c) - 3]
            if (len(stack) > 0 and stack[-1] == openbracket):
                stack.pop();
                stack.pop();
            else:
                tempstack = [c, l];
                # try finding the "correct" open bracket by "mining" the main stack and storing in a temporary stack
                while len(stack) > 0 and stack[-1] != openbracket:
                    tempstack.append(stack.pop())
                    tempstack.append(stack.pop())

                # remove that open bracket if exist
                if len(stack) > 0:
                    stack.pop()
                    stack.pop() # this index can be listed too, but i'll list only the closing brackets

                # restore the main stack
                while len(tempstack) > 0:
                    stack.append(tempstack.pop())

                # determine the index of the wrongly-closed bracket
                stack.pop()
                errindex.append(stack.pop())
        # print(str(i) + ": " + str(stack))
    while len(stack) > 0:
        stack.pop()
        errindex.append(stack.pop())
    # print(errindex)
    return errindex

def main1():
    f = open('sample.txt', 'r', encoding='UTF-8')
    text = f.read() 
    text = text + '\n'
    # print(len(text))
    result = scan(text, current=0, list_token=[])
    s = ""
    lines = []
    lineCount = 1
    for each in result:
        try:
            i = libBracket.index(each[1])
            token = each[0]
            s += token[-1]
            lines.append(lineCount)
        except: 
            if each[1] == 'whitespace':
                token = each[0]
                try:
                    i = token.index('\n')
                    lineCount += 1
                except:
                    pass

    # print(s)
    # print(lines)
    errindex = checkLinesOfBracket(s,lines)
    if len(errindex) > 0:
        print("Ngoặc lỗi tại các dòng:" + str(errindex))
    else: print("Ngoặc ko lỗi")

main1()


# ---- x-- x x----     --  ------      ----    --   xxx   x x   xx
# []{}[}[][}[}[][][{{{{{}{]{}{}{}[}[}[}{}{}{]{(()]}))))}}])})]]])]
#                 1   43 21       26354     578  678
#     7   6 5       42           3         1           123 4 567

#           1         2         3         4         5         6
# 0123456789012345678901234567890123456789012345678901234567890123


