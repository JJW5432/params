from string import letters, digits, punctuation
from os import environ
#print environ
def dec(n):
    digit_list = []
    for char in n:
        if char in letters + punctuation:
            digit_list.append(ord(char) - 55)
        elif char in digits:
            digit_list.append(int(char))
        else:
            digit_list.append(0)
    out = 0
    digit_list.reverse()
    for i in range(len(digit_list)):
        out += digit_list[i] * 16**i
    return out

def sanitize(url):
    url = url.replace('+', ' ')
    for i in range(len(url)):
        char = url[i]
        if char == '%':
            code = url[i+1:i+3]
            url = url[:i] + ord(dec(code)) + url[i+3:]
    return url

def is_number(n, dot= False):
    for char in n:
        if char not in digits + ( '.' if dot else '' ):
            return False
    return True

def html(s):
    if 'HTTP_HOST' in environ:
        return "<p>" + s + "</p>"
    else:
        return s

def verify(key, tipe):
    if type(tipe) == list:
        if None in tipe: return True
        elif type(key) in tipe: return True
        else: return False
    else:
        if tipe == None: return True
        elif type(key) == tipe: return True
        else: return False


def get_params(repl={}, allow={}, double=False, error='Error: <param> supplied more than once, using the leftmost value.', debug=False):
    params = {}
    if len(environ['QUERY_STRING']) == 0:
        return params
    for var in environ['QUERY_STRING'].split('&'):
        key, value = var.split('=')
        key, value = sanitize(key), sanitize(value)
        if key in repl: key = repl[key]
        if is_number(value): value = int(value)
        elif is_number(value, True): value = float(value)
        if double and key in params:
            print html(error.replace('<param>',key) )
        if (allow and key in allow and verify(value, allow[key]) ) or (not allow):
            if debug: print html(key + ": " + str(value))
            params[key] = value
    return params
