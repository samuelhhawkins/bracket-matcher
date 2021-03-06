def bracket_matcher(input):
    # empty stack
    catch = []
    # all the brackets
    brackets = {'[':']', '{':'}', '(':')'}
    # loop through input
    for i in input:
        # catch the keys and append to stack
        if i in brackets.keys(): catch.append(i)
        # look for other side of brackets
        if i in brackets.values():
            # if not brackets pop outa catch and return false
            if brackets[catch.pop()] != i: return False
            
    if len(catch) != 0: return False
    else: return True

print(bracket_matcher('abc(123)'))
# returns true

print(bracket_matcher('a[b]c(123'))
# # returns false -- missing closing parens
#
print(bracket_matcher('a[bc(123)]'))
# # returns true
#
print(bracket_matcher('a[bc(12]3)'))
# # returns false -- improperly nested
#
print(bracket_matcher('a{b}{c(1[2]3)}'))
# # returns true
#
print(bracket_matcher('a{b}{c(1}[2]3)))'))
# # returns false -- improperly nested
#
print(bracket_matcher('())'))
# # returns true
#
print(bracket_matcher('[]'))
# # returns false - no opening bracket to correspond with last character
#
print(bracket_matcher('abc123yay'))
# # returns true -- no brackets = correctly matched
