"""
Write a function that is given a string and returns a boolean indicating whether
that string has balanced parentheses. The string may have characters other than
parentheses, and should be ignored. e.g. 'x()' is balanced, '((y(z' is not, 'a(b())' is balanced, ')()(' is not.
"""

def is_balanced(s):

    stack = []
    for c in s:
        if(c == "("):
            stack.append(c)
        elif(c == ")"):
            if(len(stack)>0):
                stack.pop()
            else:
                return False

    if(len(stack) == 0):
        return True
    else:
        return False


    # endPos = -1
    # startPos = -1
    # for i in range(0, len(s)):
    #     c = s[i]
    #     if(c == ")"):
    #         if(endPos < 0):
    #             endPos = i
    #     elif(c == "("):
    #         if(startPos < 0):
    #             startPos = i
    #     print(str(startPos) + ":" + str(endPos))
    # if(endPos < startPos):
    #     return False
    # return True


def test_is_balanced():
    l = ['()', 'x()', '((y(z', 'a(b())', ')()(', '()()', '(((', ')', 'hi', 'h', '(']
    for s in l:
        if is_balanced(s):
            print("{} is balanced!".format(s))
        else:
            print("{} isn't balanced :(".format(s))

if __name__ == '__main__':
    test_is_balanced()
