

def parse_number(s):
    expo = False
    minus = False
    period = False
    for c in s:
        #65 - 90 upper case
        #97 - 122 lower case
        #lowercase e 101
        #"." is 46
        #"-" is 45
        order = ord(c)
        if order >= 65 and order <= 90:
            return False
        elif order >= 97 and order <= 122:
            if order == 101:
                if expo == True:
                    return False
                else:
                    expo = True
            else:
                return False
        elif order == 46:
            if expo == True or period == True:
                return False
            else:
                period = True
        elif order == 45:
            if minus == True:
                return False
            else:
                minus = True
                
    return True

print(parse_number("12.3"))
# True

print(parse_number("12a"))
# False

print(parse_number("12e2"))
# True

print(parse_number("12e"))
# True